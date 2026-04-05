from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
options = ChromeOptions()
options.add_experimental_option('detach', True)
driver=Chrome(options=options)

driver.get('https://www.flipkart.com')
sleep(2)
cross = driver.find_element(By.XPATH, "//span[@class='b3wTlE']")
cross.click()
sleep(2)
search = driver.find_element(By.XPATH, '//input[@class="nw1UBF v1zwn25"]')
search.send_keys('key chain')
sleep(2)
button = driver.find_element(By.XPATH, '//button[@class="XFwMiH"]')
button.click()
sleep(2)
price = driver.find_element(By.XPATH, '(//a[@class="pIpigb"]/..//div[@class="hZ3P6w"])[5]')
print('Price For Silver KeyChain', price.text)
