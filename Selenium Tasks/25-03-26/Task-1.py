from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

driver.get('https://www.saucedemo.com/')
driver.find_element(By.ID,'user-name').send_keys('admin')
driver.find_element(By.ID,'password').send_keys('holla')
driver.find_element(By.ID,'login-button').click()
expected = 'https://www.saucedemo.com/inventory.html'
actual = driver.current_url
if expected == actual:
    pass
else:
    import os
    # driver.save_screenshot('screenshot3.png')
    folder = os.path.join(os.getcwd(), 'screenshot')
    os.makedirs(folder,exist_ok=True)
    driver.save_screenshot(f'{folder}/screenshot1.png')

