from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://demowebshop.tricentis.com/')
driver.implicitly_wait(10)
def test_register():
    driver.find_element(By.XPATH, '//a[@class="ico-register"]').click()
def test_gender():
    # driver.find_element(By.XPATH, '(//div[@class="inputs"])').send_keys(driver.find_element(By.ID, 'gender-male').click())
    driver.find_element(By.ID, 'gender-male').click()
def test_fname():
    driver.find_element(By.ID, 'FirstName').send_keys('Shiven')
def test_lname():
    driver.find_element(By.ID, 'LastName').send_keys('Chahar')
def test_email():
    driver.find_element(By.ID, 'Email').send_keys('Shiven@gmail.com')
def test_password():
    driver.find_element(By.ID, 'Password').send_keys('asdfghjkl')
def test_confpassword():
    driver.find_element(By.ID, 'ConfirmPassword').send_keys('asdfghjkl')


