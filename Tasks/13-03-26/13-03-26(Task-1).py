# Question 1 : Using ID
# --> Open Amazon
# --> Click on Update Location

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.get('https://amazon.in')
sleep(3)
location = driver.find_element(By.ID, 'glow-ingress-line2')
location.click()

