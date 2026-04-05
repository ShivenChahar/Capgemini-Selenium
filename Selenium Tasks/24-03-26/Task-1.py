from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
options=ChromeOptions()
options.add_experimental_option("detach",True)
driver=Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://x.com/")
driver.maximize_window()
# actions=ActionChains(driver)
# ele=driver.find_element(By.XPATH,"//iframe[@title='Sign in with Google Button']")
# sleep(3)
# driver.switch_to.frame(ele)
# sleep(2)
# driver.find_element(By.XPATH,"//div[@class='nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb oXtfBe-l4eHX']").click()
driver.switch_to.frame(0)
driver.find_element(By.CLASS_NAME,'nsm7Bb-HzV7m-LgbsSe-BPrWId').click()