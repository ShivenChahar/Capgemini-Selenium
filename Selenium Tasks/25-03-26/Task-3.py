from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://www.lenskart.com/')
driver.implicitly_wait(10)
driver.find_element(By.ID,'lrd1').click()
expected = 'https://www.lenskart.com/eyeglasses.html'
actual = driver.current_url
assert actual == expected, "You are on Wrong Path"
driver.find_element(By.ID,'sortByDropdown').click()
driver.find_element(By.XPATH,'//option[text()="Most Viewed"]').click()
driver.save_screenshot('screenshot(3).png')
sleep(4)
driver.quit()
