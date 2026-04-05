from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)

########################    X-PATH    ###################################

# driver.get('https://demoqa.com/text-box')
# Name = driver.find_element(By.XPATH, '//input[@placeholder = "Full Name"]')
# Name.send_keys('Shiven')
# Email = driver.find_element(By.XPATH, '//input[@placeholder = "name@example.com"]')
# Email.send_keys('shiven@gmail.com')
# Add = driver.find_element(By.XPATH, '//textarea[@placeholder = "Current Address"]')
# Add.send_keys('Jaipur')
# sleep(2)
# # Button = driver.find_element(By.XPATH, '//button[@id= "submit"]').click()
# driver.find_element(By.XPATH, "//button[.='Submit']").click()

########################    X-PATH(USING INDEXING FOR MULTIPLE ELEMENTS)    ###################################

driver.get('https://amazon.com/')
sleep(5)
driver.find_element(By.XPATH, '(//span[@class="navFooterDescText"])[9]').click()

########################    X-PATH(USING CON)    ###################################