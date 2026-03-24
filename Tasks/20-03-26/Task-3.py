from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options=ChromeOptions()
options.add_experimental_option("detach",True)
driver=Chrome(options=options)
driver.get("https://www.bmrc.co.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//span[@class='link top-navcustom-text ']").click()
dropdown1=driver.find_element(By.XPATH,"//select[@class='form-control select fare-selects']")
option=Select(dropdown1)
option.select_by_value("WHTM")
dropdown2=driver.find_element(By.XPATH,"(//select[@class='form-control select fare-selects'])[2]")
option2=Select(dropdown2)
option2.select_by_value("BTML")
sleep(5)
driver.quit()