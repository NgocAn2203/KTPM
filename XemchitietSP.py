from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.get('https://hasaki.vn/')

driver.set_window_size(1400, 800)
driver.implicitly_wait(40)
driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
driver.find_element(By.CSS_SELECTOR, '.actions > button').click()
driver.implicitly_wait(20)

driver.find_element(By.ID, 'search').click()
driver.find_element(By.ID, 'search').send_keys('son')
driver.find_element(By.CSS_SELECTOR, '.actions > button').click()
driver.find_element(By.CLASS_NAME, 'item_list_cate').click()

results = driver.find_elements(By.CLASS_NAME, 'item_list_cate')

info = driver.find_element(By.CLASS_NAME, 'name_detail')
print(info.text)
info = driver.find_element(By.CLASS_NAME, 'txt_price')
print(info.text)
info = driver.find_element(By.CLASS_NAME, 'table_info_sp')
print(info.text)

driver.close()
# thêm comment
