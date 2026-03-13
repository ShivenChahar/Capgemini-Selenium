from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

'''driver.get('https://demoqa.com/text-box')
driver.maximize_window()
# driver.find_element(By.ID, 'userName').send_keys('Shiven Ji')  This is the way to get a elements ID and send our responses to that element by using the send_keys (tag).
username = driver.find_element(By.ID, 'userName')    # Here we assigned this get ID to a new variable.
email = driver.find_element(By.ID, 'userEmail')
add = driver.find_element(By.ID, 'currentAddress')
permanentAddress = driver.find_element(By.ID, 'permanentAddress')
username.send_keys('Shiven Ji')      # And in this step we added our main tag (send_keys) with our variable to send the value to the element.
email.send_keys('shivenji@gmail.com')
add.send_keys('Jaipur')
permanentAddress.send_keys('Hanumangarh')
submit = driver.find_element(By.ID, 'submit').click()'''

#  Amazon Web-Page  (Action By ID Locator)

# driver.get('https://www.amazon.com/')
# sleep(5)
# search = driver.find_element(By.ID, 'twotabsearchtextbox')
# searchButton = driver.find_element(By.ID, 'nav-search-submit-button')
# search.send_keys('Apple 17 pro')
# sleep(3)
# searchButton.click()

#  Amazon Web-Page  (Action By NAME Locator)

# driver.get('https://www.amazon.com/')
# sleep(5)
# search = driver.find_element(By.NAME, 'field-keywords')
# search.send_keys('helllo world')

#  Amazon Web-Page  (Action By CLASS Locator)

# driver.get('https://www.amazon.com/')
# sleep(5)
# search = driver.find_element(By.CLASS_NAME, 'nav-input.nav-progressive-attribute')   # Here comes two different elements but there Classes are same so the identifier gets confused and only takes the first element both times.
# searchButton = driver.find_element(By.CLASS_NAME, 'nav-input.nav-progressive-attribute')
# search.send_keys('Apple 17 pro')
# sleep(3)
# searchButton.click()
# driver.quit()

#  Demoqa Web-Page  (Action By TAG Locator)   {Tag name is common for several tags, So in this case the first Tag element will fetch the value.}

# driver.get('https://demoqa.com/text-box')
#
# search = driver.find_element(By.TAG_NAME, 'input')
# searchButton = driver.find_element(By.TAG_NAME, 'textarea')
# search.send_keys('Shiven')
# searchButton.send_keys('Jaipur')
# sleep(10)
# driver.quit()

# Amazon Web-Page  (Action By LINK TEXT Locator)

# driver.get('https://www.amazon.in/')
# sleep(5)
# # search = driver.find_element(By.PARTIAL_LINK_TEXT, 'Sell')
# searchButton = driver.find_element(By.LINK_TEXT, 'Customer Service')
# # search.click()
# # sleep(2)
# searchButton.click()
# sleep(5)
# driver.quit()

###############################################################################
# CSS Selectors

driver.get('https://www.amazon.in/')
sleep(5)
