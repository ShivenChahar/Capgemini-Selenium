from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
options=ChromeOptions()
options.add_experimental_option("detach",True)
driver=Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
alert=driver.switch_to.alert
sleep(2)
print(alert.text)
alert.accept()

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
alert=driver.switch_to.alert
sleep(2)
print(alert.text)
alert.accept()

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
alert=driver.switch_to.alert
sleep(2)
alert.send_keys("Shiven Chahar")
print(alert.text)
alert.accept()

