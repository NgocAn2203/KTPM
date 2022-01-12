from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://hotro.hasaki.vn/lien-he.html')

str = input('Hãy nhập tiêu đề: ')
inp = driver.find_element(By.NAME,'title')
inp.send_keys(str)

str = input('Hãy nhập chi tiết: ')
inp = driver.find_element(By.NAME,'detail')
inp.send_keys(str)

str = input('Hãy nhập Họ Tên bạn: ')
inp = driver.find_element(By.NAME,'fullname')
inp.send_keys(str)

str = input('Hãy nhập sdt: ')
inp = driver.find_element(By.NAME,'phone')
inp.send_keys(str)


str = input('Hãy nhập mail: ')
inp = driver.find_element(By.NAME,'email')
inp.send_keys(str)

driver.find_element(By.ID,'submit').click()
driver.implicitly_wait(15)

title = driver.find_element(By.XPATH,'//*[@id="contact-noti"]/div/div/div[1]/div/h6').text()
print(title)

