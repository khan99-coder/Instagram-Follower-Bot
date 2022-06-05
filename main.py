from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
import os


CHROME_DRIVER_PATH = "C:\Development2\chromedriver.exe"
SIMILAR_ACCOUNT = "python.learning"
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
INSTAGRAM_URL = " https://www.instagram.com/accounts/login/"


class InstaFollower:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        sleep(2)
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(5)

        sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.XPATH, "//div[@class='isgrP']")
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

