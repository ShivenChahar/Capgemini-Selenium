from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
options=ChromeOptions()
options.add_experimental_option("detach",True)
driver=Chrome(options=options)
driver.implicitly_wait(10)
driver.get('https://www.zomato.com/chennai/restaurants/')
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@class='sc-3o0n99-5 jqszCs']").click()
sleep(3)
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="auth-login-ui"]'))
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Sign in with Google Button']"))
driver.find_element(By.XPATH, "//span[text()='Sign in with Google']").click()
sleep(7)
driver.quit()