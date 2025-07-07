from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pytest

@pytest.fixture(params=[
    ("chrome", (1920, 1080)),
    ("chrome", (1366, 768)),
    ("chrome", (375, 667)),
    ("firefox", (1920, 1080)),
    ("firefox", (1366, 768)),
    ("firefox", (375, 667))
    ], ids=[
        "chrome_1920x1080",
        "chrome_1366x768",
        "chrome_375x667",
        "firefox_1920x1080",
        "firefox_1366x768",
        "firefox_375x667",
    ])
def setup(request):

    # get environment or default one
    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    detach = os.getenv("DETACH", "false").lower() == "true"

    browser, resolution = request.param
    width, height = resolution

    if browser =="chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        if detach:
            options.add_experimental_option("detach", True)
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size={}x{}".format(width, height))
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("browser.privatebrowsing.autostart", True)
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    if not headless:
        driver.set_window_size(width=width, height=height)

    driver.get(base_url)
    yield driver

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



