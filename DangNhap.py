from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://hasaki.vn/')

driver.implicitly_wait(20)
driver.find_element(By.ID,"onesignal-slidedown-cancel-button").click()
print(driver.title)

driver.find_element(By.ID, "btn-login").click()
driver.implicitly_wait(5)
with open('TestCase.csv', newline='') as f:
   reader = csv.DictReader(f)
   for row in reader:
       u = row['user']
       p = row['password']

(driver.find_element(By.ID,'username')).send_keys(u)
(driver.find_element(By.ID,'password')).send_keys(p)
(driver.find_element(By.CLASS_NAME,'btn_site_1')).click()
driver.implicitly_wait(15)

