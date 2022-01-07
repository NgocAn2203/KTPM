from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get('https://hasaki.vn/')

driver.implicitly_wait(20)
driver.find_element(By.ID,"onesignal-slidedown-cancel-button").click()
driver.find_element(By.XPATH,'//*[@id="v3_wrapper_container"]/div[1]/div[7]/div[2]/div[1]/div/ul/li[2]/div').click()
driver.find_element(By.ID,"config_op_42").click()
driver.find_element(By.XPATH,'//*[@id="product_addtocart_form"]/div[3]/div/div/div[4]').click()
#driver.find_element(By.ID,'notifyWhenAvailable').click()

with open('ThongTin.csv',newline='') as f:
    reader=csv.DictReader(f)
    for row in reader:
        t = row['hoten']
        e = row['sdtemail']
driver.find_element(By.XPATH,'//*[@id="notify-form"]/div/div/div/div').click()
(driver.find_element(By.ID,'notify-fullname')).send_keys(t)
(driver.find_element(By.ID,'notify-email')).send_keys(e)
driver.find_element(By.ID,'sendNotifyStock').click()
driver.implicitly_wait(8)