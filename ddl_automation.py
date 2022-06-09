# Python script to Control your chrome browser using selenium 
# RUN pip install selenium  https://pypi.org/project/selenium/
# download selenium driver from https://chromedriver.chromium.org/home 

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import os
from dotenv import load_dotenv
load_dotenv()

#change as per requirement
chrome_path = "/Users/jonyeatman/Downloads/chromedriver"
email = os.environ.get("EMAIL")
password  = os.environ.get("PASSWD")
url = os.environ.get("URL")
ddl = 'Fridge 12'
date = '06/07/2022'


print("process Started ---------")

op = Options()
op.add_argument("--start-maximized") #open Browser in maximized mode
op.add_argument("--no-sandbox") #bypass OS security model
op.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
# op.add_experimental_option("excludeSwitches", ["enable-automation"])
# op.add_experimental_option('useAutomationExtension', False)
op.headless = False # change to true if we want to hide the browser
s = Service(chrome_path)

with  webdriver.Chrome(service=s, options=op) as d:
    d.get(url)
    d.find_element(by=By.XPATH, value='//*[@id="login-form:j_idt123_content"]/div[1]/div[2]/div/input').send_keys(email)
    d.find_element(by=By.XPATH, value='//*[@id="login-form:j_idt123_content"]/div[2]/div[2]/div/input').send_keys(password)
    d.find_element(by=By.XPATH, value='//*[@id="login-form:j_idt136"]/span').click()
    time.sleep(3)
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:config-name-filter-table:0:devices-panel-config-name-filter-input"]').send_keys(ddl)
    time.sleep(5)
   #  d.find_element(by=By.TAG_NAME, value='gridcell').click()
    
   #  handles = d.window_handles
   #  for handle in handles:
   #    d.switch_to.window(handle)

   #  d.close()

print("Done----------------------")

#  d.find_element(By.ID, "user_password").send_keys(password)
# d.switch_to.window(windows[1])


