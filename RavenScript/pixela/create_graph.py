import requests
import os
import dotenv
dotenv.load_dotenv('.env')
TOKEN = os.getenv("pixela_token")
USERNAME = "lizhaoxue"


header = {"X-USER-TOKEN": TOKEN}
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_config = {
    "id": "dev100",
    "name": "100-days-of-development-in-Python",
    "unit": "commit",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Dubai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# response.raise_for_status()
# print(response.json())


# Post a pixel
graph_id = "dev100"
pixel_endpointt = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}"

body_config = {
    "date": "20231215",
    "quantity": "4"
}

response = requests.post(url=pixel_endpointt, json=body_config, headers=header)
print(response.text)


# delete a graph
# graphid = "test-graph"
# graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graphid}"
# response = requests.delete(url=graph_endpoint,headers=header)
# print(response.text)

# update pixel
# dt = "20231210"
# update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/dev100/{dt}"
# update_info = {
#     "quantity": "10"
# }
# response = requests.put(url=update_endpoint, json=update_info, headers=header)
# print(response.text)


# Get a graph in SVG format
# svg_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/dev100/"
# response = requests.get(svg_endpoint).text
# with open("img.svg", "w") as f:
#     f.write(response)


