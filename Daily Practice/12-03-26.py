'''from time import sleep
from selenium.webdriver import Chrome
driver = Chrome()
sleep(5)'''
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
options = ChromeOptions()
options.add_experimental_option("detach", True)  # If we use False here all these commands will not execute!
driver = Chrome(options=options)  # We must declare the above variable here because it is the command which is holding the browser.

# To open a web-page.
driver.get('https://amazon.in')  # This is a command which is passed to open a particular web-page.
# return-type for this is => NONE

#   --(3)--BROWSER WINDOW METHODS-----

# (1.)To Minimize a web-page.
# driver.minimize_window()
# sleep(3)
# return-type for this is => NONE

# (2.)To Maximize a web-page.
# driver.maximize_window()
# sleep(2)
# return-type for this is => NONE

# (3.)To Full_Screen a web-page.
# driver.fullscreen_window()
# return-type for this is => NONE

#   --(3)--PAGE VERIFICATION METHODS----

# (1.) To fetch the Title
# title = driver.title
# print(title)

# (2.)To fetch the URL for the Current Web-Page.
# print(driver.current_url)

# (3.)To fetch the Source for the Web-Page.
# print(driver.page_source)

# Assgning a variable
name = driver.name
print(name)

# -----CLOSE & QUIT-----
# sleep(5)  # This sleep time is req. to add some new tags along with our main tab.
# IN Close suppose we opened some other tabs along with our main tab, So the close will only close our main tab.
# driver.close()
#  IN Quit tag if the same situation is there, the whole screen will collapse along with all the tabs.
# driver.quit()

sleep(5)
driver.back()
sleep(5)
driver.forward()
