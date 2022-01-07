from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get('https://hasaki.vn/')

driver.implicitly_wait(20)
driver.find_element(By.ID,"onesignal-slidedown-cancel-button").click()
driver.find_element(By.XPATH,'//*[@id="v3_wrapper_container"]/div[1]/div[7]/div[2]/div[1]/div/ul/li[2]/div').click()
driver.find_element(By.ID,"config_op_27").click()
driver.find_element(By.ID,"product-addtocart-button").click()

