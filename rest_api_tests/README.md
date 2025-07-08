# REST API Testing Project with Python
This project uses [ReqRes](https://reqres.in/) public API. The solution is built in **Python** using **Pytest**, **Requests**, and **Selenium (for ApiKey scraping)** to simulate key user actions and perform validations.

---

## 📋 Scenario Steps Covered

| Step | Description |
|------|-------------|
| 1️⃣  | **List available users** using `GET /api/users?page=1` |
| 2️⃣  | **Extract single user details** (ID and email) |
| 3️⃣  | **Sort all users by first name alphabetically** and print them |
| 4️⃣  | **Get extracted user details** using `GET /api/users/{USER_ID}` |
| 5️⃣  | **Try to get details of a non-existing user** and verify `404` |
| 6️⃣  | **Create a unique user** using `POST /api/users` |
| 7️⃣  | **Delete the newly created user** using `DELETE /api/users/{USER_ID}` |
| 8️⃣  | **Parameterize base URL** via environment variable or user input |

---

## ⚙️ Setup and Run Instructions

1. Create a virtual environment:

   ```bash
   python -m venv venv
2. Activate the environment:

   ```bash
   venv\Scripts\activate.ps1
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
4. Run tests:
    ```bash
    python run_tests.py
- When prompted, you can provide a custom environment URL or press Enter to use the default: https://reqres.in/