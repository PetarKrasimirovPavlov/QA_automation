# QA Automation Challenge



## 🔧 Version 1 

### ✅ Scenario 1 – Complete Purchase Flow

1. Log in using the standard user credentials from the index page 
2. Add the first and last item from the inventory to the cart
3. Verify both items are added correctly
4. Remove the first item from the cart
5. Add the item before the last one from the inventory
6. Verify the cart content again
7. Proceed to checkout
8. Complete the order
9. Verify the order is placed successfully
10. Confirm the cart is empty after purchase
11. Log out from the system

---

### ✅ Scenario 2 – Sorting Verification

1. Log in with the standard user
2. Select the sorting option **"Price (high to low)"**
3. Verify that the displayed items are sorted in correct descending order by price
4. Log out from the system

---

## 🚀 How to Run the Tests

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

   - To run all tests:

     ```bash
     pytest -v
     ```

   - To run only specific scenarios:

     ```bash
     pytest -m scenario1
     ```

     ```bash
     pytest -m scenario2
     ```