from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

driver.get('https://wikipedia.com')
sleep(2)
driver.refresh()
print(driver.title)

driver.get('https://www.amazon.com/')
sleep(5)
print(driver.title)
driver.back()
sleep(5)
driver.close()
