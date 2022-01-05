from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://hasaki.vn/')

driver.implicitly_wait(20)
driver.find_element(By.ID,"onesignal-slidedown-cancel-button").click()
print(driver.title)

with open('TestCaseDK.csv', newline='') as f:
 reader = csv.DictReader(f)
 for row in reader:
     e = row['email']
     p = row['password']
     f = row['fullname']

driver.find_element(By.CLASS_NAME, "popup-register").click()
(driver.find_element(By.NAME,'email')).send_keys(e)
(driver.find_element(By.NAME,'password')).send_keys(p)
(driver.find_element(By.NAME,'fullname')).send_keys(f)
driver.find_element(By.ID, 'btnRegister').click()
driver.implicitly_wait(3)


