import requests
import json



headers = {"x-api-key":"reqres-free-v1"}
response = requests.get("https://reqres.in//api/users?page=1", headers=headers)


assert response.status_code == 200
assert response.json()["page"] == 1
assert response.json()["total_pages"] == 2

data = response.json()["data"]

print(f"First user details are: ID: {data[0]["id"]},  first_name:{data[0]["first_name"]}, Last name: {data[0]["last_name"]}, email: {data[0]["email"]},")

