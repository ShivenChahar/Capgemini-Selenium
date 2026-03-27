from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://www.amazon.in/')
driver.implicitly_wait(10)
search = (driver.find_element(By.ID,'twotabsearchtextbox'))
search.send_keys('phone')
suggestion4 = driver.find_element(By.ID,'sac-suggestion-row-4').click()
sortby = driver.find_element(By.XPATH,'//span[@class="a-button-text a-declarative"]').click()
newest = driver.find_element(By.ID,'s-result-sort-select_4').click()
freeship = driver.find_element(By.XPATH,'(//i[@class="a-icon a-icon-checkbox"])[3]').click()
# sleep(3)
device = driver.find_element(By.XPATH,'(//h2[contains(@class , "a-size-medium a-spacing-none")])[1]')
price = driver.find_element(By.CLASS_NAME,'a-price-whole')
a = (device.text)
b = (price.text)
print(a,'=',b)
