import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

class ApiKey:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_key(self):
        ''' This function uses selenium for webscraping the free ApiKey from Reqres website'''

        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.get(self.base_url)
        driver.find_element(by=By.XPATH, value = '//*[text()="🆓 GET FREE API KEY"]').click()
        key, value = driver.find_element(by=By.CLASS_NAME, value = "header-code").text.split(": ")
        headers = {key:value}
        return headers


class APIAction:
    def __init__(self, base_url, headers: ApiKey ):
        self.base_url = base_url
        self.headers = headers.get_key()

    def get_users(self, page: int):
        '''This function gets all users from page as per arguments'''
        return requests.get(f"{self.base_url}/api/users", headers=self.headers, params={"page":page})

    def get_user_details(self, id: int):
        '''This function gets specific user details as per arguments'''
        return requests.get(f"{self.base_url}/api/users/{id}", headers=self.headers)
    
    def create_user(self, name: str, job: str):
        '''This function creates user as per arguments'''
        return requests.post(f"{self.base_url}/api/users", headers=self.headers, json={"name": name, "job": job})
    
    def delete_user(self, id: int):
        '''This function deletes user as per id in arguments'''
        return requests.delete(f"{self.base_url}/api/users/{id}", headers=self.headers)
    
        
