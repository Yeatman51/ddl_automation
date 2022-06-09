# Python script to Control your chrome browser using selenium 
# RUN pip install selenium  https://pypi.org/project/selenium/
# download selenium driver from https://chromedriver.chromium.org/home 

import time, os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()

#change as per requirement
chrome_path = "/Users/jonyeatman/Downloads/chromedriver"
email = os.environ.get("EMAIL")
password  = os.environ.get("PASSWD")
url = os.environ.get("URL")

ddl = 'Fridge 11'
ddl2 = 'Fridge 12'
ddl3 = 'Freezer 18'
date = 'June 03, 2022'


print("process Started ---------")

op = Options()
op.add_argument("--start-maximized") #open Browser in maximized mode
op.add_argument("--no-sandbox") #bypass OS security model
op.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option('useAutomationExtension', False)
op.headless = False # change to true if we want to hide the browser
s = Service(chrome_path)

with  webdriver.Chrome(service=s, options=op) as d:
    d.get(url)
    d.find_element(by=By.XPATH, value='//*[@id="login-form:j_idt123_content"]/div[1]/div[2]/div/input').send_keys(email)
    d.find_element(by=By.XPATH, value='//*[@id="login-form:j_idt123_content"]/div[2]/div[2]/div/input').send_keys(password)
    d.find_element(by=By.XPATH, value='//*[@id="login-form:j_idt136"]/span').click()
    time.sleep(2)
# ddl input
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:config-name-filter-table:0:devices-panel-config-name-filter-input"]').send_keys(ddl)
    time.sleep(2)
# drop-down
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-filter-input"]').click()
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-filter-input"]').send_keys(Keys.ARROW_UP, Keys.ENTER)
    time.sleep(2)
# date input
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-to-filter-input_input"]').send_keys(date)
    time.sleep(2)
# data table
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:devices-table_data"]/tr[2]/td[3]/a').click()
    time.sleep(3)
# export
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:j_idt400_content"]/table/tbody/tr[10]/td/a').click()
    time.sleep(3)
# run report
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-builder-form:runBtn"]').click()
    time.sleep(12)
# home
    d.find_element(by=By.ID, value='j_idt40:j_idt42').click()
    time.sleep(3)
# rerun

# ddl input
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:config-name-filter-table:0:devices-panel-config-name-filter-input"]').send_keys(ddl2)
    time.sleep(2)
# drop-down
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-filter-input"]').click()
    time.sleep(2)
# date input
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-to-filter-input_input"]').send_keys(date)
    time.sleep(2)
# data table
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:devices-table_data"]/tr[2]/td[3]/a').click()
    time.sleep(3)
# export
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:j_idt400_content"]/table/tbody/tr[10]/td/a').click()
    time.sleep(3)
# run report
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-builder-form:runBtn"]').click()
    time.sleep(12)
# home
    d.find_element(by=By.ID, value='j_idt40:j_idt42').click()
    time.sleep(3)
# rerun

# ddl input
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:config-name-filter-table:0:devices-panel-config-name-filter-input"]').send_keys(ddl3)
    time.sleep(2)
# drop-down
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-filter-input"]').click()
    time.sleep(2)
# date input
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:date-filter-table:0:devices-panel-date-to-filter-input_input"]').send_keys(date)
    time.sleep(2)
# data table
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:devices-table_data"]/tr[2]/td[3]/a').click()
    time.sleep(3)
# export
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-devices-form:j_idt400_content"]/table/tbody/tr[10]/td/a').click()
    time.sleep(3)
# run report
    d.find_element(by=By.XPATH, value='//*[@id="intempconnect-data-builder-form:runBtn"]').click()
    time.sleep(12)
# home
    d.find_element(by=By.ID, value='j_idt40:j_idt42').click()
    time.sleep(3)


print("Done----------------------")

#  d.find_element(By.ID, "user_password").send_keys(password)
# d.switch_to.window(windows[1])

  #  handles = d.window_handles
   #  for handle in handles:
   #    d.switch_to.window(handle)

   #  d.close()

