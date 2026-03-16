# Question 4 : Using LINK TEXT and PARTIAL LINK TEXT
# --> Open https://www.selenium.dev/
# --> Fetch Page title
# --> Click on 'Downloads'
# --> Click on 'Other Languages Exist'
# --> Click on 'Register Now'


from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://www.selenium.dev/')
print(driver.title)
sleep(2)
driver.find_element(By.LINK_TEXT, 'Downloads').click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, 'other languages exist').click()
sleep(2)
driver.find_element(By.LINK_TEXT, 'Register now!').click()

