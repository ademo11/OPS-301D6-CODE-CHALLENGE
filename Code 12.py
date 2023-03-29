import requests

# Prompt user for input
url = input("Enter the destination URL: ")
method = input("Select a HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the request to the screen and confirm before proceeding
print(f"Sending {method} request to {url}")
confirmation = input("Proceed with request? (y/n): ")
if confirmation.lower() != 'y':
    exit()

# Send request and print response header information
response = requests.request(method, url)
print(f"\nResponse Headers:\n")
for key, value in response.headers.items():
    if key.lower() == 'content-length':
        print(f"{key}: {int(value)/1024:.2f} KB")
    else:
        print(f"{key}: {value}")

# Translate status code to plain terms for the 10 most common codes
status_codes = {
    200: 'OK',
    201: 'Created',
    204: 'No Content',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Site not found',
    500: 'Internal Server Error',
    503: 'Service Unavailable',
    504: 'Gateway Timeout'
}

print(f"\nStatus Code: {response.status_code} ({status_codes.get(response.status_code, 'Unknown status code')})")

# Reference
# OpenAI