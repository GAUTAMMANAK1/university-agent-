import http.client

# Establish connection to the API host
conn = http.client.HTTPSConnection("University-by-Location-API.proxy-production.allthingsdev.co")

# Define the payload and headers
payload = "{\r\n    \"university\": \"mahatma\"\r\n}"
headers = {
   'x-api-key': 'aMFouLkMjcxGopFBPmzjWGMKQCkVKPDMsghukTvPHaPWzsqALZZFfGRtpBgvEKVVLGDJjDBavveHcoVKhuqjovsRWhkgGEQiyRmX',
   'x-app-version': '1.0.0',
   'x-apihub-key': 'DyLv9weLZw3hr3iUVMNN5iJrFQALu1E34C6o5Vf5UvrYk6naMY',
   'x-apihub-host': 'University-by-Location-API.allthingsdev.co'
}

# Send the POST request with payload and headers
conn.request("POST", "/api/v1/university/get", payload, headers)

# Get the response
res = conn.getresponse()

# Read the response data
data = res.read()

# Print the response data
print(data.decode("utf-8"))
