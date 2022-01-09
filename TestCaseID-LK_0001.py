# coding = utf-8
# encoding : utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv
import time

driver = webdriver.Chrome(executable_path='venv/Scripts/chromedriver.exe')
driver.set_window_size(1300, 700)
driver.get('https://hasaki.vn/')
driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
print(driver.title)
print('******************')
driver.implicitly_wait(2)
try:
    with open('BO_01_06_07_08_09.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            u = row['SDT']
            p = row['HoTen']
        driver.find_element(By.XPATH, '//*[@id="box_icon_category"]/div/div/div[7]').click()
        time.sleep(1)  #trì hoãn thực thi khoảng 3s
        driver.find_element(By.NAME, 'phone').send_keys(u)
        driver.find_element(By.NAME, 'fullName').send_keys(p)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

        driver.find_element(By.XPATH,
                            '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
        driver.find_element(By.XPATH, '//*[@id="block_input_time"]/div[3]/div/div[3]').click()  # Chọn thời gian khác
        time.sleep(1)
        driver.find_element(By.ID, 'btnBooking').click()
        time.sleep(1)
        # info = driver.find_element(By.XPATH, '//*[@id="booking_sussces_page"]/div/div[2]/a')   #width_common block_info_succes
        info = driver.find_element(By.CLASS_NAME, 'block_info_success')
        print(info.text)
        time.sleep(1)

except Exception as ex:
    print('Lỗi')
    print()
    print(ex)

    time.sleep(1)
    driver.quit()
