import requests
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "picpinic1@3",
    "username": "lizhaoxue",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixela_endpoint, json=user_params)
print(response.json())

# Get the token and save to env

