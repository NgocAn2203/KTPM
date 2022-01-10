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
with open('MK-003.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        a = row['sdt']
        b = row['password']
        c = row['pass']
        d = row['npass']
        e = row['rpass']

(driver.find_element(By.ID, "username")).send_keys(a)
(driver.find_element(By.ID, "password")).send_keys(b)
driver.implicitly_wait(2)
driver.find_element(By.CLASS_NAME, 'btn_site_1').click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH,'//*[@id="bar_menu"]').click()
#driver.find_element(By.ID,'wrapper_menu').click()
driver.find_element(By.XPATH,'//*[@id="main_menu_site"]/div[3]/div/div[3]/a').click()
#river.find_element((By.XPATH,'//*[@id="profile_page"]/div[1]/div[1]')).click()
driver.find_element(By.XPATH,'//*[@id="profile_page"]/div[1]/div[1]/div[2]/a[4]').click()
(driver.find_element(By.ID,'password')).send_keys(c)
(driver.find_element(By.ID,'passwordNew')).send_keys(d)
(driver.find_element(By.ID,'passwordConfirm')).send_keys(e)

driver.find_element(By.XPATH,'//*[@id="form-account"]/div[2]/div/button').click()
driver.implicitly_wait(20)
#  MK-001 MK-002 MK-005
#error=driver.find_element(By.XPATH,'//*[@id="form-account"]/div[2]').text

# MK-003 MK-007 MK-008
error=driver.find_element(By.XPATH,'//*[@id="passwordConfirm-error"]').text
# MK-004
#error=driver.find_element(By.XPATH,'//*[@id="password-error"]').text
# MK-006
#error=driver.find_element(By.XPATH,'//*[@id="passwordNew-error"]').text

print(error)
driver.implicitly_wait(90)
driver.quit()