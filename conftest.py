import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import requests


with open("./testdata.yaml") as f:
   testdata = yaml.safe_load(f)
   
name = testdata["username"]
passwd = testdata['password']

@pytest.fixture()
def er1():
   return "401"

@pytest.fixture()
def er2():
   return "Hello, {}".format(name)


@pytest.fixture(scope="session")
def browser():
    # if browser == "firefox":
    #     service = Service(executable_path=GeckoDriverManager().install())
    #     options = webdriver.FirefoxOptions()
    #     driver = webdriver.Firefox(service=service, options=options)
    # elif browser == "chrome":
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
    
    
# API    
  
@pytest.fixture()
def login():
   r = requests.post('https://test-stand.gb.ru/gateway/login', data={'username': name, 'password': passwd})
   return r.json()['token']

@pytest.fixture()
def text1():
   return 'Something like that 1'

@pytest.fixture()
def text2():
   return 'test content'
    





