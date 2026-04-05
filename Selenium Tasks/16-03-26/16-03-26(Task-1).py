from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
options = ChromeOptions()
options.add_experimental_option('detach', True)
driver=Chrome(options=options)

driver.get('https://www.amazon.com')
sleep(3)
search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('Iphone')
sleep(2)
click = driver.find_element(By.ID, 'nav-search-submit-button').click()
apple = driver.find_element(By.XPATH, "//span[text()='Apple iPhone 16 Pro, 256GB, Natural Titanium for Verizon (Renewed)']/../../../..//span[@class='a-price-whole']").text
print('Price Apple', apple)
sleep(10)
driver.close()