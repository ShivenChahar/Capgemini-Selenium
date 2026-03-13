# Question 2 : Using Name
# --> Open Facebook
# --> Enter email and password

from asyncio import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://www.facebook.com')
email = driver.find_element(By.NAME, 'email')
email.send_keys('shiven@gmail.com')
sleep(3)
password = driver.find_element(By.NAME, 'pass')
password.send_keys('12345678')
sleep(3)

