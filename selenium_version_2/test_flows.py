from common_actions import setup, standard_login, extract_inventory, extract_cart, add_product_to_cart, logout, open_cart, teardown
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.scenario1
def test_flow_scenario_1(setup):
    driver = setup
    standard_login(driver)

    product_list = extract_inventory(driver)

    assert len(product_list) > 1, "Inventory has less than 2 products — test requires at least two!"

    wishlist = [product_list[0], product_list[-1]]

    # adding products to cart
    for product in wishlist:
        add_product_to_cart(driver, product)

    open_cart(driver)

    # Cart content verification
    assert set(wishlist) == set(extract_cart(driver))

    # removing first product
    product_str = "-".join([word.lower() for word in wishlist[0].split()])
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,f"remove-{product_str}"))).click()
    wishlist.remove(wishlist[0])

    # clicking "Continue Shopping" button
    driver.find_element(by=By.ID, value="continue-shopping").click()

    # refetching inventory product list
    product_list = extract_inventory(driver)
    previous_to_last = product_list[-2]

    # Adding previous to last product in cart
    add_product_to_cart(driver, previous_to_last)
    wishlist.append(previous_to_last)

    open_cart(driver)

    # Cart content verification
    assert set(wishlist) == set(extract_cart(driver))

    # Checking out
    driver.find_element(by=By.ID, value = "checkout").click()

    # Finishing the order
    driver.find_element(by=By.ID, value = "first-name").send_keys("Test_First_Name")
    driver.find_element(by=By.ID, value = "last-name").send_keys("Test_Last_Name")
    driver.find_element(by=By.ID, value = "postal-code").send_keys("Test_Code")
    driver.find_element(by=By.ID, value = "continue").click()

    # Order content verification
    assert set(wishlist) == set(extract_cart(driver))

    driver.find_element(by=By.ID, value = "finish").click()

    # Succesfull order checks
    assert "checkout-complete" in driver.current_url
    assert "Complete!" in driver.find_element(by=By.CLASS_NAME, value="title").text 
    assert "Thank you for your order!" in WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text

    driver.find_element(by=By.CLASS_NAME, value = "shopping_cart_link").click()

    # Cart content verification
    assert 0 == len(extract_cart(driver))

    # Logging out
    logout(driver)

@pytest.mark.scenario2
def test_flow_scenario_2(setup):
    driver = setup
    standard_login(driver)

    # sorting by Price (high to low)
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container"))).click()
    select_class = driver.find_element(by=By.CLASS_NAME, value="product_sort_container")
    select = Select(select_class)
    select.select_by_visible_text("Price (high to low)")

    # Active sort option varification
    assert "Price (high to low)" == WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME, "active_option"))).text
    
    prices = driver.find_elements(by=By.CLASS_NAME, value="inventory_item_price")

    # Verifying enough prices(products) are available
    assert len(prices) > 1, "Inventory has less than 2 products — test requires at least two!"

    price_list = [float(price.text[1:]) for price in prices]
    # Verifying correct sequence
    assert price_list==sorted(price_list, reverse=True)

    # Logging out
    logout(driver)