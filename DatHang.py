from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

# from selenium.common import exceptions


# from selenium.common.exceptions.InvalidArgumentException


driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://hasaki.vn/sales/order/history/')
print(driver.title)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
driver.find_element(By.ID, "btn-login").click()
driver.implicitly_wait(5)
with open('DH-001.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        a = row['sdt']
        b = row['password']
        c = row['HoTen']
(driver.find_element(By.ID, "username")).send_keys(a)
(driver.find_element(By.ID, "password")).send_keys(b)
driver.implicitly_wait(2)
driver.find_element(By.CLASS_NAME, 'btn_site_1').click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//*[@id="v3_header"]/div[2]/div[3]/div[1]/a[1]').click()
driver.find_element(By.CLASS_NAME, 'btn_site_2').click()
(driver.find_element(By.NAME, 'fullName').send_keys(c))
driver.find_element(By.CSS_SELECTOR, '#checkoutSteps a span').click()

driver.implicitly_wait(70)

driver.quit()
