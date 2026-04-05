from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
options=ChromeOptions()
options.add_experimental_option("detach",True)
driver=Chrome(options=options)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//img[@src='https://demowebshop.tricentis.com/content/images/thumbs/0000201_build-your-own-expensive-computer_125.jpeg']").click()
driver.find_element(By.XPATH,"//a[@href='/apparel-shoes']").click()
dropdown1=driver.find_element(By.ID,"products-orderby")
option=Select(dropdown1)
option.select_by_index(3)
dropdown2=driver.find_element(By.ID,"products-pagesize")
option2=Select(dropdown2)
option2.select_by_index(2)
dropdown3=driver.find_element(By.ID,"products-viewmode")
option3=Select(dropdown3)
option3.select_by_visible_text('Grid')

sleep(5)
driver.quit()
