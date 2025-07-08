from api_actions import APIAction, ApiKey
import os

# get environment or default one
base_url = os.getenv("BASE_URL", "https://reqres.in/")

# create API Key instance
api_key = ApiKey(base_url)

# create Action instance
api = APIAction(base_url, api_key)


def test_list_users():
    response = api.get_users(1)

    assert response.status_code == 200
    assert response.json()["page"] == 1
    assert response.json()["total_pages"] == 2
    assert len(response.json()["data"]) != 0

    # extract single user details (Id, Email)
    first_user_data = response.json()["data"][0]
    first_user = {"id": first_user_data["id"],
                    "email": first_user_data["email"]}
    print(f"First user id: {first_user['id']}, email: {first_user['email']} ")

    # Extract all users, sort them by First Name alphabetically. Print sorted collection.
    all_users = response.json()["data"]
    sorted_all_users = sorted(all_users, key = lambda user: user["first_name"])
    print("Printing users collection sorted alphabetically by first name bellow:")
    for user in sorted_all_users:
        print(user)

def test_existing_user_details():
    users_list_response = api.get_users(1)

    # extract single user
    first_user_id = users_list_response.json()["data"][0]["id"]
    assert isinstance(first_user_id, int)

    response = api.get_user_details(first_user_id)

    assert response.status_code == 200
    assert response.json()["data"]["email"]
    assert response.json()["data"]["first_name"]
    assert response.json()["data"]["last_name"]

def test_non_existing_user_details():
    response = api.get_user_details(-1)

    assert response.status_code == 404
    assert response.json() == {}

def test_create_unique_user():
    name = "John"
    job = "Tester"

    response = api.create_user(name, job)

    assert response.status_code == 201
    assert response.json()["name"] == name
    assert response.json()["job"] == job

def test_delete_new_user():
    name = "John"
    job = "Tester"

    creation_response = api.create_user(name, job)

    # Note: Created user has fake id. API responds always with status code 204 for user deletion. Create + deletion flow is made for challange purposes.
    response = api.delete_user(creation_response.json()["id"])

    assert response.status_code == 204
    


