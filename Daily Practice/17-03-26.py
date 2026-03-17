from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
button = driver.find_element(By.XPATH, "//button[text()='Start']").click()
driver.implicitly_wait(20)
hello = driver.find_element(By.ID, "finish").text
print(hello)