# Question 3 : Using ID and PARTIAL LINK TEXT
# --> Open Amazon
# --> Search for Mobiles (use ID)
# --> Click on any 1 mobile (use PARTIAL LINK TEXT)

from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://www.amazon.com/')
sleep(2)
search=driver.find_element(By.ID,'twotabsearchtextbox')
search.send_keys('Mobiles')
sleep(2)
searchButton=driver.find_element(By.ID,'nav-search-submit-button')
searchButton.click()
sleep(2)
mobile=driver.find_element(By.PARTIAL_LINK_TEXT,'Samsung Galaxy S26')
mobile.click()