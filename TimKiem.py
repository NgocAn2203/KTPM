from selenium import webdriver
from selenium.webdriver.common.by import By

sp = input("Nhap san pham ban muon tim: ")
driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.get('https://hasaki.vn/')

driver.set_window_size(1400, 800)
driver.implicitly_wait(40)
driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
driver.find_element(By.CSS_SELECTOR, '.actions > button').click()
driver.implicitly_wait(20)


driver.find_element(By.ID, 'search').click()
driver.find_element(By.ID, 'search').send_keys(sp)
driver.find_element(By.CSS_SELECTOR, '.actions > button').click()

results = driver.find_elements(By.CLASS_NAME, 'item_list_cate')
if results:
    for item in results:
        driver.implicitly_wait(20)
        content = item.find_element(By.TAG_NAME, 'a')
        print(content.text)
        print(content.get_attribute('data-brand'))
        title = item.find_element(By.TAG_NAME, 'h2').text
        print(title)
        print(content.get_attribute('href'))
        print('---------')
    driver.close()
else:
    print('Rất tiếc, không tìm thấy sản phẩm')
