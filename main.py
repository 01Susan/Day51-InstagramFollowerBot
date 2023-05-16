import os

from navigation import Navigation
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
site = "https://www.instagram.com/"
test = Navigation(username, password, site)
test.login()
test.navigate(accountname="name of account")
test.follow()
