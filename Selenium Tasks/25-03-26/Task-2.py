from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get(' https://in.pinterest.com/')
driver.implicitly_wait(10)
driver.save_screenshot('MainPage(2).png')
image = driver.find_element(By.XPATH,'(//img[@class="iFOUS5 ALBw9Q"])[13]')
action = ActionChains(driver)
action.scroll_to_element(image).pause(3).perform()
driver.save_screenshot('Image(2).png')
sleep(5)
driver.quit()