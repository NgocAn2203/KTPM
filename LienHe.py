from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get('https://hotro.hasaki.vn/lien-he.html')

with open('LienHe.csv',newline='') as f:
    reader=csv.DictReader(f)
    for row in reader:
        t = row['tieude']
        c = row['chitiet']
        n = row['ten']
        s = row['sdt']
        e = row['email']

(driver.find_element(By.ID,'contact_title')).send_keys(t)
(driver.find_element(By.ID,'contact_detail')).send_keys(c)
(driver.find_element(By.ID,'contact_fullname')).send_keys(n)
(driver.find_element(By.ID,'contact_phone')).send_keys(s)
(driver.find_element(By.ID,'contact_email')).send_keys(e)
driver.find_element(By.ID,'submit').click()
