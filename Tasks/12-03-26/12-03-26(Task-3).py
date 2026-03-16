'''Write a script to:
-> navigate to a Wikipedia
-> Refresh
-> Fetch title
-> Open amazon
-> Fetch title
-> Go back
-> Close'''

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

options = ChromeOptions()
options.add_experimental_option("detach",True)
driver = Chrome(options=options)
driver.get("https://wikipedia.com")
driver.refresh()
print(driver.title)
driver.get("https://amazon.in/")
sleep(2)
print(driver.title)
sleep(2)
driver.back()
driver.close()