from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep


class Navigation:
    def __init__(self, username, password, site):
        # Initialize the Navigation class with the provided username, password, and site URL
        self.username = username
        self.password = password
        self.site = site
        self.options = Options()
        self.options.add_argument("--disable-notifications")
        self.chrome_path = r"D:\Downloads\chromedriver_win32\chromedriver.exe"
        self.service = Service(self.chrome_path)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def login(self):
        # Method to login to the website
        self.driver.get(self.site)
        self.driver.maximize_window()
        sleep(4)

        # Find the email input element and enter the username
        email_element = self.driver.find_element(by=By.NAME, value="username")
        email_element.send_keys(self.username)
        print("email written")
        sleep(2)

        # Find the password input element and enter the password
        password_element = self.driver.find_element(by=By.NAME, value="password")
        password_element.send_keys(self.password)
        print("password written")
        sleep(2)

        # Find the login button element and click it to login
        login_element = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
        login_element.click()
        print("logged in")

    def navigate(self,  account_name):
        # Method to navigate to a specific profile and scroll through followers
        sleep(8)

        # Handle any pop-up notifications
        turn_off_notifications = self.driver.find_element(By.XPATH, '/html/body')
        turn_off_notifications.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)
        sleep(3)

        # Visit a specific profile URL
        self.driver.get(f"https://www.instagram.com/{ account_name}/")
        sleep(4)

        # Click on the "followers" link to view the followers
        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
        followers.click()
        sleep(4)

        # Find the scroll bar element and scroll down multiple times
        scroll_bar = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for _ in range(5):
            sleep(2)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_bar)

    def follow(self):
        # Method to follow users from the list of followers
        sleep(4)

        # Find all the follow buttons on the page
        buttons = self.driver.find_elements(By.CSS_SELECTOR, value="div._aano button._acan._acap._acas._aj1-")
        print(len(buttons))

        # Click on each follow button, handling any click interception exceptions
        for button in buttons:
            try:
                sleep(2)
                button.click()
            except ElementClickInterceptedException:
                sleep(2)
                # If the button click is intercepted, find
                cancel_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel_button.click()
        self.driver.quit()
