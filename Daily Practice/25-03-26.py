import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

##############################-----------(Assertion)(It is used for checking the condition if that is true or not)------------------#####################
# #{If the value is True, then the code will just pass to the next line----but if there is mismatch in assertion, then the code will not move ahead}
# driver.get("https://www.google.com")
# driver.implicitly_wait(10)
# driver.maximize_window()
# print(driver.title)
# expected  = 'Google'
# actual = driver.title
# assert expected == actual, "Title is Mismatch"
# driver.quit()
#################################----------(Task)---(How to take a ScreenShot)--------#################################3
# driver.get("https://www.amazon.in/")
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.find_element(By.XPATH, "(//div[@class='nav-div'])[6]").click()
# expected = 'https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers'
# actual = driver.current_url
#
# assert expected == actual, "You are on wrong page"
# driver.save_screenshot('screenshot1.png')                             #--------------Screenshot
# driver.quit
#######################################(How to Take SS and Store in a Folder)################################################################
# import os
# driver.get("https://www.google.com")
# driver.implicitly_wait(10)
# driver.maximize_window()
# folder=os.path.join(os.getcwd(),'screenshot')               # This is how we make a folder
# os.makedirs(folder,exist_ok=True)                           # We are make the directories
# driver.save_screenshot(f'{folder}/screenshot.png')          # This is how we save the SS in particular Folder.

##############################---------Element screenshot
# element = driver.find_element(By.XPATH,'//div[@class="k1zIA rSk4se"]')
# # element.screenshot(f'{folder}/screenshot.png')
#
# timestamp=time.strftime("%Y%m%d-%H%M%S")
# element.screenshot(f'{folder}/screenshot_ele_{timestamp}.png')
# # driver.quit()

driver.get('https://www.saucedemo.com/')
driver.find_element(By.ID,'user-name').send_keys('admin')
driver.find_element(By.ID,'password').send_keys('holla')
driver.find_element(By.ID,'login-button').click()
expected = 'https://www.saucedemo.com/inventory.html'
actual = driver.current_url
if expected == actual:
    pass
else:
    driver.save_screenshot('screenshot2.png')

