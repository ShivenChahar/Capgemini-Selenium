from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
options=ChromeOptions()
options.add_experimental_option("detach",True)
driver=Chrome(options=options)
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

sleep(6)
driver.quit()