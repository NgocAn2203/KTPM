# coding = utf-8
# encoding : utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

class DatHen:   # Nhớ thay đổi thời gian đặt hẹn trước khi chạy
    def BO_01(self):
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
                driver.find_element(By.NAME, 'phone').send_keys(u)
                driver.find_element(By.NAME, 'fullName').send_keys(p)
                driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[3]/div/div[1]').click()  #Chọn thời gian khác
                driver.implicitly_wait(10)
                driver.find_element(By.ID, 'btnBooking').click()
                info = driver.find_element(By.CLASS_NAME, 'block_info_success')
                print(info.text)
                driver.implicitly_wait(10)

        except Exception as ex:
            print('Lỗi')
            print()
            print()
            print(ex)

            driver.implicitly_wait(10)
            driver.quit()

    def BO_02(self):
        driver = webdriver.Chrome(executable_path='venv/Scripts/chromedriver.exe')
        driver.set_window_size(1300, 700)
        driver.get('https://hasaki.vn/')
        driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
        print(driver.title)
        print('******************')
        driver.implicitly_wait(2)
        try:
            with open('BO_02.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['SDT']
                    p = row['HoTen']
                driver.find_element(By.XPATH, '//*[@id="box_icon_category"]/div/div/div[7]').click()
                driver.find_element(By.NAME, 'phone').send_keys(u)
                driver.find_element(By.NAME, 'fullName').send_keys(p)

                driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[3]/div/div[3]').click()  # Chọn thời gian khác

                driver.find_element(By.ID, 'btnBooking').click()
                # info = driver.find_element(By.XPATH, '//*[@id="booking_sussces_page"]/div/div[2]/a')   #width_common block_info_succes
                info = driver.find_element(By.CLASS_NAME, 'block_info_success')
                print(info.text)
                driver.implicitly_wait(10)

        except Exception as ex:
                print('Lỗi')
                print('Vui lòng nhập số điện thoại! ')
                print()
                print(ex)

                driver.implicitly_wait(10)
                driver.quit()

    def BO_03(self):
        driver = webdriver.Chrome(executable_path='venv/Scripts/chromedriver.exe')
        driver.set_window_size(1300, 700)
        driver.get('https://hasaki.vn/')
        driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
        print(driver.title)
        print('******************')
        driver.implicitly_wait(2)
        try:
            with open('BO_03.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['SDT']
                    p = row['HoTen']
                driver.find_element(By.XPATH, '//*[@id="box_icon_category"]/div/div/div[7]').click()
                driver.find_element(By.NAME, 'phone').send_keys(u)
                driver.find_element(By.NAME, 'fullName').send_keys(p)
                driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[3]/div/div[3]').click()  # Chọn thời gian khác

                driver.find_element(By.ID, 'btnBooking').click()
                # info = driver.find_element(By.XPATH, '//*[@id="booking_sussces_page"]/div/div[2]/a')   #width_common block_info_succes
                info = driver.find_element(By.CLASS_NAME, 'block_info_success')
                print(info.text)
                driver.implicitly_wait(10)

        except Exception as ex:
            print('Lỗi')
            print('Số điện thoại không hợp lệ! ')
            print()
            print(ex)

            driver.implicitly_wait(10)
            driver.quit()

    def BO_04(self):
        driver = webdriver.Chrome(executable_path='venv/Scripts/chromedriver.exe')
        driver.set_window_size(1300, 700)
        driver.get('https://hasaki.vn/')
        driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
        print(driver.title)
        print('******************')
        driver.implicitly_wait(2)
        try:
            with open('BO_04.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['SDT']
                    p = row['HoTen']
                driver.find_element(By.XPATH, '//*[@id="box_icon_category"]/div/div/div[7]').click()
                driver.find_element(By.NAME, 'phone').send_keys(u)
                driver.find_element(By.NAME, 'fullName').send_keys(p)
                driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[3]/div/div[3]').click()  # Chọn thời gian khác

                driver.find_element(By.ID, 'btnBooking').click()
                # info = driver.find_element(By.XPATH, '//*[@id="booking_sussces_page"]/div/div[2]/a')   #width_common block_info_succes
                info = driver.find_element(By.CLASS_NAME, 'block_info_success')
                print(info.text)
                driver.implicitly_wait(10)

        except Exception as ex:
            print('Lỗi')
            print('Vui lòng nhập họ tên! ')
            print()
            print(ex)

            driver.implicitly_wait(10)
            driver.quit()

    def BO_05(self):
        driver = webdriver.Chrome(executable_path='venv/Scripts/chromedriver.exe')
        driver.set_window_size(1300, 700)
        driver.get('https://hasaki.vn/')
        driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
        print(driver.title)
        print('******************')
        driver.implicitly_wait(2)
        try:
            with open('BO_05.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['SDT']
                    p = row['HoTen']
                driver.find_element(By.XPATH, '//*[@id="box_icon_category"]/div/div/div[7]').click()
                driver.find_element(By.NAME, 'phone').send_keys(u)
                driver.find_element(By.NAME, 'fullName').send_keys(p)
                driver.implicitly_wait(10)
                driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[3]/div/div[3]').click()  # Chọn thời gian khác

                driver.find_element(By.ID, 'btnBooking').click()
                # info = driver.find_element(By.XPATH, '//*[@id="booking_sussces_page"]/div/div[2]/a')   #width_common block_info_succes
                info = driver.find_element(By.CLASS_NAME, 'block_info_success')
                print(info.text)
                driver.implicitly_wait(10)

        except Exception as ex:
            print('Lỗi')
            print('Họ tên không hợp lệ! ')
            print()
            print(ex)

            driver.implicitly_wait(10)
            driver.quit()

    def BO_06(self):
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
                driver.find_element(By.NAME, 'phone').send_keys(u)
                driver.find_element(By.NAME, 'fullName').send_keys(p)
                #driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[3]/div/div[3]').click()  # Chọn thời gian khác

                driver.find_element(By.ID, 'btnBooking').click()
                # info = driver.find_element(By.XPATH, '//*[@id="booking_sussces_page"]/div/div[2]/a')   #width_common block_info_succes
                info = driver.find_element(By.CLASS_NAME, 'block_info_success')
                print(info.text)
                driver.implicitly_wait(10)

        except Exception as ex:
            print('Lỗi')
            print('Vui lòng chọn chi nhánh! ')
            print()
            print(ex)

            driver.implicitly_wait(10)
            driver.quit()

    def BO_07(self):
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
                driver.find_element(By.NAME, 'phone').send_keys(u)
                driver.find_element(By.NAME, 'fullName').send_keys(p)
                driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
                #driver.find_element(By.XPATH, '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
                driver.find_element(By.XPATH,
                                    '//*[@id="block_input_time"]/div[3]/div/div[3]').click()  # Chọn thời gian khác

                driver.find_element(By.ID, 'btnBooking').click()
                # info = driver.find_element(By.XPATH, '//*[@id="booking_sussces_page"]/div/div[2]/a')   #width_common block_info_succes
                info = driver.find_element(By.CLASS_NAME, 'block_info_success')
                print(info.text)
                driver.implicitly_wait(10)

        except Exception as ex:
            print('Lỗi')
            print('Vui lòng chọn danh mục! ')
            print()
            print(ex)

            driver.implicitly_wait(10)
            driver.quit()

    def BO_08(self):
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
                driver.find_element(By.NAME, 'phone').send_keys(u)
                driver.find_element(By.NAME, 'fullName').send_keys(p)
                driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
                driver.find_element(By.XPATH, '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

                #driver.find_element(By.XPATH, '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
                #driver.find_element(By.XPATH,'//*[@id="block_input_time"]/div[3]/div/div[3]').click()  # Chọn thời gian khác
                driver.implicitly_wait(10)
                driver.find_element(By.ID, 'btnBooking').click()
                # info = driver.find_element(By.XPATH, '//*[@id="booking_sussces_page"]/div/div[2]/a')   #width_common block_info_succes
                info = driver.find_element(By.CLASS_NAME, 'block_info_success')
                print(info.text)
                driver.implicitly_wait(10)

        except Exception as ex:
            print('Lỗi')
            print('Vui lòng chọn thời gian đặt hẹn! ')
            print()
            print(ex)

            driver.implicitly_wait(10)
            driver.quit()

    def BO_09(self):
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
                driver.find_element(By.NAME, 'phone').send_keys(u)
                driver.find_element(By.NAME, 'fullName').send_keys(p)
                driver.find_element(By.XPATH, '//*[@id="block_input_chinhanh"]/div[2]/div[2]/ul/li[2]/div/span').click()
                driver.find_element(By.XPATH, '//*[@id="block_input_danhmuc"]/div[1]/div[2]/div[2]/ul/li[2]/div/span').click()

                driver.find_element(By.XPATH, '//*[@id="block_input_time"]/div[2]/div[2]/div[2]/ul/li[4]/div').click()  # Chọn thời gian khác
                driver.find_element(By.XPATH,'//*[@id="block_input_time"]/div[3]/div/div[3]').click()  # Chọn thời gian khác
                driver.implicitly_wait(10)
                driver.find_element(By.ID, 'btnBooking').click()
                # info = driver.find_element(By.XPATH, '//*[@id="booking_sussces_page"]/div/div[2]/a')   #width_common block_info_succes
                info = driver.find_element(By.CLASS_NAME, 'block_info_success')
                print(info.text)
                driver.implicitly_wait(10)

        except Exception as ex:
            print('Lỗi')
            print()
            print(ex)

            driver.implicitly_wait(10)
            driver.quit()

Test = DatHen()
#Test.BO_01()
#Test.BO_02()
#Test.BO_03()
#Test.BO_04()
#Test.BO_05()
#Test.BO_06()
#Test.BO_07()
Test.BO_08()
#Test.BO_09()

