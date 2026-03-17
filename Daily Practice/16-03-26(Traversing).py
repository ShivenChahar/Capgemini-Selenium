from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
options = ChromeOptions()
options.add_experimental_option('detach', True)
# options.add_argument('--headless')
driver=Chrome(options=options)

##########Task - 1##########
# driver.get('http://demoqa.com/webtables')
# salary = driver.find_element(By.XPATH,"//td[text() = 'Cierra']/..//td[5]")
# print('Salary of Cierra', salary.text)

#########Task - 2############
# driver.get('https://the-internet.herokuapp.com/tables')
# due = driver.find_element(By.XPATH,"//td[text() = 'Frank']/..//td[4]")
# print('Due of Frank', due.text)

###########Task - 3#############we are Capturing the Dynamic Element(Which keeps on Changing) by the help of its main element which is Static (So we don't get error if the dynamuc value changes)
# driver.get('https://www.amazon.com')
# sleep(3)
# search = driver.find_element(By.ID, 'twotabsearchtextbox')
# search.send_keys('Iphone')
# sleep(2)
# click = driver.find_element(By.ID, 'nav-search-submit-button').click()
# # sam = driver.find_element(By.XPATH,"//span[text()='Samsung Galaxy S26 Ultra, Unlocked Android Smartphone + $200 Gift Card, 512GB, Privacy Display, Galaxy AI, AI Camera, Super Fast Charging 3.0, Durable Battery, 2026, US 1 Year Warranty, Black']/../../../..//span[@class='a-price-whole']")
# apple = driver.find_element(By.XPATH, "//span[text()='Apple iPhone 16 Pro, 256GB, Natural Titanium for Verizon (Renewed)']/../../../..//span[@class='a-price-whole']").text
# # print('Price Samsung', sam.text)
# print('Price Apple', apple)
# sleep(10)
# driver.close()

#######################Task - 4##################(Directly go onto KeyChain Page and Fetch Price for one)

driver.get('https://www.flipkart.com')
sleep(2)
cross = driver.find_element(By.XPATH, "//span[@class='b3wTlE']")
cross.click()
sleep(2)
search = driver.find_element(By.XPATH, '//input[@class="nw1UBF v1zwn25"]')
search.send_keys('key chain')
sleep(2)
button = driver.find_element(By.XPATH, '//button[@class="XFwMiH"]')
button.click()
sleep(2)
price = driver.find_element(By.XPATH, '(//a[@class="pIpigb"]/..//div[@class="hZ3P6w"])[5]')
print('Price For Silver KeyChain', price.text)
