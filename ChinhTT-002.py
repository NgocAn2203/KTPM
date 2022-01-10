from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv


driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://hasaki.vn/sales/order/history/')
print(driver.title)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
driver.find_element(By.ID, "btn-login").click()
driver.implicitly_wait(5)
with open('TT-002.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        a = row['Mail']
        b = row['password']
        c = row['Name']
        d = row['Phone']

(driver.find_element(By.ID, "username")).send_keys(a)
(driver.find_element(By.ID, "password")).send_keys(b)
driver.implicitly_wait(2)
driver.find_element(By.CLASS_NAME, 'btn_site_1').click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH,'//*[@id="bar_menu"]').click()
driver.find_element(By.XPATH,'//*[@id="main_menu_site"]/div[3]/div/div[3]/a').click()
driver.find_element(By.XPATH,'//*[@id="profile_page"]/div[1]/div[1]/div[2]/a[3]').click()
driver.find_element(By.ID,'fullName').send_keys(c)
driver.find_element(By.ID,'phone').send_keys(d)
dob_date=Select(driver.find_element(By.NAME,'dob_date'))
dob_date.select_by_visible_text("22")
dob_date=Select(driver.find_element(By.NAME,'dob_month'))
dob_date.select_by_visible_text("12")
dob_date=Select(driver.find_element(By.NAME,'dob_year'))
dob_date.select_by_visible_text("1999")
# 002
driver.find_element(By.XPATH,'//*[@id="form-account"]/div[2]/div/div[2]/div/div/div[10]/button').click()
description=driver.find_element(By.CSS_SELECTOR,'#input_info_account > div').text
print(description)
driver.quit()