from common_actions import setup, standard_login, extract_inventory, extract_cart, add_product_to_cart,logout, open_cart, teardown
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_flow_scenario_1():
    """
    End-to-end user flow test for shopping application:
    - Logs in with standard credentials.
    - Extracts inventory and adds first and last products to cart.
    - Verifies cart contents.
    - Removes the first product from the cart.
    - Adds the previous to last product from the inventory.
    - Verifies cart contents after each modification.
    - Proceeds to checkout, fills user information, and finishes the order.
    - Validates order completion messages and empty cart after order.
    - Logs out and quits the browser.
    """

    driver = None
    try:
        driver = setup()
        standard_login(driver)

        product_list = extract_inventory(driver)

        assert len(product_list) > 1, "Inventory has less than 2 products — test requires at least two!"

        wishlist = [product_list[0], product_list[-1]]

        # adding products to cart
        for product in wishlist:
            add_product_to_cart(driver, product)

        open_cart(driver)

        # Cart content verification
        assert set(wishlist) == set(extract_cart(driver)) , "Cart content do not match expected wishlist!"

        # removing first product
        product_str = "-".join([word.lower() for word in wishlist[0].split()])
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,f"remove-{product_str}"))).click()
        wishlist.remove(wishlist[0])

        # clicking "Continue Shopping" button
        driver.find_element(by=By.ID, value="continue-shopping").click()

        # refetching inventory product list (in case inventory changed)
        product_list = extract_inventory(driver)
        previous_to_last = product_list[-2]

        # Adding previous to last product in cart
        add_product_to_cart(driver, previous_to_last)
        wishlist.append(previous_to_last)

        open_cart(driver)

        # Cart content verification
        assert set(wishlist) == set(extract_cart(driver)), "Cart content do not match expected wishlist!"

        # Checking out
        driver.find_element(by=By.ID, value = "checkout").click()

        # Finishing the order
        driver.find_element(by=By.ID, value = "first-name").send_keys("Test_First_Name")
        driver.find_element(by=By.ID, value = "last-name").send_keys("Test_Last_Name")
        driver.find_element(by=By.ID, value = "postal-code").send_keys("Test_Code")
        driver.find_element(by=By.ID, value = "continue").click()

        # Order content verification
        assert set(wishlist) == set(extract_cart(driver)), "Order content do not match expected wishlist!"

        driver.find_element(by=By.ID, value = "finish").click()

        # Succesfull order checks
        assert "checkout-complete" in driver.current_url , "URL does not indicate successful checkout completion!"
        assert "Complete!" in driver.find_element(by=By.CLASS_NAME, value="title").text , "Page title does not confirm successful order completion!"
        assert "Thank you for your order!" in driver.find_element(by=By.CLASS_NAME, value = "complete-header").text , "Order confirmation message is missing in UI!"

        driver.find_element(by=By.CLASS_NAME, value = "shopping_cart_link").click()

        # Cart content verification
        assert 0 == len(extract_cart(driver)) , "Cart is not emptied after order completion."

        # Logging out
        logout(driver)

    finally:
        teardown(driver)


def test_flow_scenario_2():
    """
    Test sorting functionality on inventory page:
    - Logs in with standard credentials.
    - Sorts products by price, from high to low.
    - Verifies that the active sort option is correctly displayed.
    - Validates that product prices are sorted in descending order.
    - Logs out and quits the browser.
    """

    driver = None
    try:
        driver = setup()
        standard_login(driver)

        # sorting by Price (high to low)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container"))).click()
        select_class = driver.find_element(by=By.CLASS_NAME, value="product_sort_container")
        select = Select(select_class)
        select.select_by_visible_text("Price (high to low)")

        # Active sort option verification
        assert "Price (high to low)" == driver.find_element(by=By.CLASS_NAME, value="active_option").text , "Active sort option is incorrect or missing!"

        # Verifying correct sequence
        prices = driver.find_elements(by=By.CLASS_NAME, value="inventory_item_price")

        # Virifying enough prices(products) are available
        assert len(prices) > 1, "Inventory has less than 2 products — test requires at least two!"

        price_list = [float(price.text[1:]) for price in prices]
        assert price_list==sorted(price_list, reverse=True) , "Product prices are not sorted from high to low as expected."

        # Logging out
        logout(driver)

    finally:
        teardown(driver)
