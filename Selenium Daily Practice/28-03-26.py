from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.get('https://www.naukri.com/')
driver.implicitly_wait(10)

