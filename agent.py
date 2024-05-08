import requests
from ai_engine import KeyValue, UAgentResponse, UAgentResponseType
from pydantic import BaseModel, Field

# Define the API endpoint and headers
UNIVERSITY_API_URL = "https://University-by-Location-API.proxy-production.allthingsdev.co/api/v1/university/get"
HEADERS = {
    'x-api-key': 'aMFouLkMjcxGopFBPmzjWGMKQCkVKPDMsghukTvPHaPWzsqALZZFfGRtpBgvEKVVLGDJjDBavveHcoVKhuqjovsRWhkgGEQiyRmX',
    'x-app-version': '1.0.0',
    'x-apihub-key': 'DyLv9weLZw3hr3iUVMNN5iJrFQALu1E34C6o5Vf5UvrYk6naMY',
    'x-apihub-host': 'University-by-Location-API.allthingsdev.co'
}

class UniversityRequest(BaseModel):
    location: str = Field(description="Location to search for university details")

def fetch_university_data(location):
    payload = {"university": location}
    response = requests.post(UNIVERSITY_API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def handle_message(sender, msg):
    print(f"Received message from {sender}.")
    try:
        location = msg.location
        if location:
            university_data = fetch_university_data(location)
            if university_data:
                options = [KeyValue(key=str(idx), value=uni["name"]) for idx, uni in enumerate(university_data)]
                response = UAgentResponse(options=options, type=UAgentResponseType.SELECT_FROM_OPTIONS)
                print({"status": "success", "response": response.dict()})
            else:
                response = UAgentResponse(message="No university data available for this location.",
                                          type=UAgentResponseType.FINAL)
                print({"status": "error", "response": response.dict()})
        else:
            response = UAgentResponse(message="Location parameter missing in the request.",
                                      type=UAgentResponseType.ERROR)
            print({"status": "error", "response": response.dict()})
    except Exception as exc:
        response = UAgentResponse(message=str(exc), type=UAgentResponseType.ERROR)
        print({"status": "error", "response": response.dict()})

if __name__ == "__main__":
    # Example usage
    message = UniversityRequest(location="mahatma")
    handle_message("sender_id", message)
