from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.get('https://hasaki.vn/')

driver.set_window_size(1300, 700)
driver.implicitly_wait(20)
driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
driver.implicitly_wait(20)
driver.find_element(By.ID, 'search').click()
driver.find_element(By.ID, 'search').send_keys('Kem chống nắng')
driver.find_element(By.CSS_SELECTOR, '.actions > button').click()