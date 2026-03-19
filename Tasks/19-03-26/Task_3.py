
""" Task-3: Open Demo Webshop
and register yourself"""
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"gender-female").click()
driver.find_element(By.ID,"FirstName").send_keys("Shiven")
driver.find_element(By.ID,"LastName").send_keys("Chahar")
driver.find_element(By.ID,"Email").send_keys("shiven@gmail.com")
driver.find_element(By.ID,"Password").send_keys("1230")
driver.find_element(By.ID,"ConfirmPassword").send_keys("1230")
driver.find_element(By.NAME,"register-button").click()