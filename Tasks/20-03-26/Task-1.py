from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes for")
sleep(2)
prod=driver.find_elements(By.XPATH,'//div[@class="s-suggestion s-suggestion-ellipsis-direction"]')
sleep(2)
for i in prod:
    print(i.text)
prod[4].click()