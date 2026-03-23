from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from websocket import send
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@class='sc-dBfaGr dyyfrm']").click()
driver.find_element(By.XPATH,"//input[@class='sc-dBfaGr dyyfrm']").send_keys("dosa")
dishes=driver.find_elements(By.XPATH,"//p[@class='sc-1hez2tp-0 sc-gFXMyG jkvifB']")
for i in dishes:
    print(i.text)
dishes[2].click()