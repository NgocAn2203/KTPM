# coding = utf-8
# encoding : utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import csv
import time

driver = webdriver.Chrome(executable_path='venv/Scripts/chromedriver.exe')
driver.set_window_size(1300, 700)
driver.get('https://hasaki.vn/')
driver.implicitly_wait(20)
driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
print(driver.title)
print('*****')
#print(driver.page_source)

class TraCuuDonHang:     #TestCase LO_01: lỗi
    def LO_01(self):   # Đã đăng nhập user

        try:
            # Đăng nhập
            driver.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
            driver.find_element(By.ID, "btn-login").click()

            with open('DangNhap.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['sdt']
                    p = row['password']

            (driver.find_element(By.ID, "username")).send_keys(u)
            (driver.find_element(By.ID, "password")).send_keys(p)
            driver.implicitly_wait(5)
            driver.find_element(By.CLASS_NAME, 'btn_site_1').click()
            driver.implicitly_wait(5)

            # Tra cứu   .block_app_topbar .check_donhang left .btn_top_right
            driver.find_element(By.CSS_SELECTOR, '#top_bar_hasaki div.relative.check_donhang.left').click()
            driver.find_element(By.ID, 'dLabel').click()
            lo = driver.find_elements(By.XPATH, '//*[@id="box_donhang_vuadat"]/div[2]/table/tbody/tr/td[1]/a')
            print(lo)
            time.sleep(1)

        except Exception as ex:
            print('Lỗi')
            print()
            print()
            print(ex)

    def LO_02(self):   #TTin đầy đủ, chưa đăng nhập

        try:
            with open('LO_02.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['MaDonHang']
                    p = row['EmailHoacSDT']
                driver.find_element(By.ID, 'dLabel').click()
                (driver.find_element(By.ID, 'order_id')).send_keys(u)
                (driver.find_element(By.NAME, 'contact')).send_keys(p)
                driver.find_element(By.CLASS_NAME, 'btnCheckOrder').click()
                # driver.find_element(By.CSS_SELECTOR, '#quick-checking-order input').click()
                driver.implicitly_wait(10)
                info = driver.find_elements(By.CSS_SELECTOR, '.relative check_donhang left .block_input_order_checking '
                                                             'dropdown-menu .text-center .btn btn_site_1 btnCheckOrder')
                driver.implicitly_wait(10)

                # LO_02: Đầy đủ ttin
                inti = driver.find_element(By.CLASS_NAME, 'info_customer_order')      #Lấy tất cả thông tin về đơn hàng
                # inti = driver.find_element(By.XPATH, '//*[@id="checking_oder_page"]/div[1]/div[1]/div[1]')   # Lấy tình trạng đơn
                print(inti.text)
                driver.implicitly_wait(10)
        except Exception as ex:
            print('Lỗi')
            print()
            print()
            print(ex)

    def LO_03(self):  # LO_03: k nhập mã đơn

        try:
            with open('LO_03.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['MaDonHang']
                    p = row['EmailHoacSDT']
                driver.find_element(By.ID, 'dLabel').click()
                (driver.find_element(By.ID, 'order_id')).send_keys(u)
                (driver.find_element(By.NAME, 'contact')).send_keys(p)
                driver.find_element(By.CLASS_NAME, 'btnCheckOrder').click()
                # driver.find_element(By.CSS_SELECTOR, '#quick-checking-order input').click()
                driver.implicitly_wait(10)
                info = driver.find_elements(By.CSS_SELECTOR, '.relative check_donhang left .block_input_order_checking '
                                                             'dropdown-menu .text-center .btn btn_site_1 btnCheckOrder')
                driver.implicitly_wait(10)

                # LO_03: k nhập mã đơn
                inti = driver.find_element(By.ID, 'order_id-error')
                print(inti.text)
                driver.implicitly_wait(10)
        except Exception as ex:
            print('Lỗi')
            print()
            print()
            print(ex)

    def LO_04(self):     # LO_04: nhập sai mã

        try:
            with open('LO_04.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['MaDonHang']
                    p = row['EmailHoacSDT']
                driver.find_element(By.ID, 'dLabel').click()
                (driver.find_element(By.ID, 'order_id')).send_keys(u)
                (driver.find_element(By.NAME, 'contact')).send_keys(p)
                driver.find_element(By.CLASS_NAME, 'btnCheckOrder').click()
                # driver.find_element(By.CSS_SELECTOR, '#quick-checking-order input').click()
                driver.implicitly_wait(10)
                info = driver.find_elements(By.CSS_SELECTOR, '.relative check_donhang left .block_input_order_checking '
                                                             'dropdown-menu .text-center .btn btn_site_1 btnCheckOrder')
                driver.implicitly_wait(10)

                # LO_04: nhập sai mã    alert alert-danger flashSession
                inti = driver.find_element(By.CLASS_NAME, 'flashSession')
                print(inti.text)
                driver.implicitly_wait(10)
        except Exception as ex:
            print('Lỗi')
            print()
            print()
            print(ex)

    def LO_05(self):    # LO_05: Không nhập SĐT

        try:
            with open('LO_05.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['MaDonHang']
                    p = row['EmailHoacSDT']
                driver.find_element(By.ID, 'dLabel').click()
                (driver.find_element(By.ID, 'order_id')).send_keys(u)
                (driver.find_element(By.NAME, 'contact')).send_keys(p)
                driver.find_element(By.CLASS_NAME, 'btnCheckOrder').click()
                # driver.find_element(By.CSS_SELECTOR, '#quick-checking-order input').click()
                driver.implicitly_wait(10)
                info = driver.find_elements(By.CSS_SELECTOR, '.relative check_donhang left .block_input_order_checking '
                                                             'dropdown-menu .text-center .btn btn_site_1 btnCheckOrder')
                driver.implicitly_wait(10)

                # LO_05: Không nhập SĐT
                inti = driver.find_element(By.ID, 'emailPhone-error')
                print(inti.text)
                driver.implicitly_wait(10)
        except Exception as ex:
            print('Lỗi')
            print()
            print()
            print(ex)

    def LO_06(self):     # LO_06: Nhập sai SĐT

        try:
            with open('LO_06.csv', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row['MaDonHang']
                    p = row['EmailHoacSDT']
                driver.find_element(By.ID, 'dLabel').click()
                (driver.find_element(By.ID, 'order_id')).send_keys(u)
                (driver.find_element(By.NAME, 'contact')).send_keys(p)
                driver.find_element(By.CLASS_NAME, 'btnCheckOrder').click()
                # driver.find_element(By.CSS_SELECTOR, '#quick-checking-order input').click()
                driver.implicitly_wait(10)
                info = driver.find_elements(By.CSS_SELECTOR, '.relative check_donhang left .block_input_order_checking '
                                                             'dropdown-menu .text-center .btn btn_site_1 btnCheckOrder')
                driver.implicitly_wait(10)

                # LO_06: Nhập sai SĐT
                inti = driver.find_element(By.XPATH, '//*[@id="v3_wrapper_container"]/'
                                                     'div[1]/div/div[1]/div[2]/div[1]/div')
                print(inti.text)
                driver.implicitly_wait(10)
        except Exception as ex:
            print('Lỗi')
            print()
            print()
            print(ex)

TestCase = TraCuuDonHang()
#TestCase.LO_01()
#TestCase.LO_02()
#TestCase.LO_03()
#TestCase.LO_04()
#TestCase.LO_05()
#TestCase.LO_06()

driver.quit()  # báo lỗi
# driver.close()
