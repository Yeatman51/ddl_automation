# Python script to Control your chrome browser using selenium 
# RUN pip install selenium  https://pypi.org/project/selenium/
# download selenium driver from https://chromedriver.chromium.org/home 

import time, os
from turtle import up
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()

# .env
chrome_path = "/Users/jonyeatman/Downloads/chromedriver"
email = os.environ.get("EMAIL")
password  = os.environ.get("PASSWD")
url = os.environ.get("URL")

ddl1 = 'Refrigerator 31'
date = 'May 1, 2022'


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
    d.find_element(by=By.NAME, value='login-form:j_idt120').send_keys(email)
    d.find_element(by=By.NAME, value='login-form:j_idt125').send_keys(password)
    d.find_element(by=By.ID, value='login-form:j_idt127').click()
    time.sleep(2)

# Refrigerator 31
# ddl input
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:config-name-filter-table:0:devices-panel-config-name-filter-input"]').send_keys(ddl1)
    time.sleep(2)
# drop-down
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-filter-input"]').send_keys('b')
    time.sleep(2)
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-filter-input"]').send_keys('b')
    time.sleep(2)
# date input
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-to-filter-input_input"]').send_keys(date)
    time.sleep(4)
# data table
# Matching value text
    d.find_element(by=By.LINK_TEXT, value='Refrigerator 31').click() 
    time.sleep(3)
# export
    d.find_element(by=By.LINK_TEXT, value='Export').click()
    time.sleep(3)
# run report
    d.find_element(by=By.ID, value='intempconnect-data-builder-form:runBtn').click()
    time.sleep(12)
# home
    d.find_element(by=By.ID, value='j_idt40:j_idt42').click()
    time.sleep(3)
# rerun



print("Done----------------------")
