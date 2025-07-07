from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup():
    options = webdriver.ChromeOptions()

    # Uncomment bellow for testing purposes.
    # options.add_experimental_option("detach", True)

    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    return driver

def standard_login(driver):

    username = driver.find_element(by=By.CLASS_NAME, value="login_credentials").text
    password = driver.find_element(by=By.CLASS_NAME, value="login_password").text

    username = username.splitlines()[1]
    password = password.splitlines()[1]

    driver.find_element(by=By.ID, value="user-name").send_keys(username)
    driver.find_element(by=By.ID, value="password").send_keys(password)

    submit_button = driver.find_element(by=By.ID, value="login-button")
    submit_button.click()

def add_product_to_cart(driver, product: str):
    product_str = "-".join([word.lower() for word in product.split()])
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,f"add-to-cart-{product_str}"))).click()

def extract_inventory(driver):
    products = driver.find_elements(by=By.CLASS_NAME, value="inventory_item_name")
    product_list = [product.text for product in products]
    return product_list

def extract_cart(driver):
    cart_products = driver.find_elements(by=By.CLASS_NAME, value = "inventory_item_name")
    cart_products_list = [product.text for product in cart_products]
    return cart_products_list

def logout(driver):
    driver.find_element(by=By.ID, value = "react-burger-menu-btn").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()



