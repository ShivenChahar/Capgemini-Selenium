# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)



#fetch all the links on google home page using find_elements
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)
links = driver.find_elements(By.TAG_NAME,"a")
#print(links) # gives the address of all the links
print(len(links)) # gives the count of links
#print the visible text or name of links
for l in links:
    print(l.text) """

#get_attribute to fetch attribute value
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)
ele = driver.find_element(By.XPATH,"//a[@class='gb_A']")
print(ele.get_attribute('aria-label')) # returns the value of aria-label attribute """

'''
driver.get("https://google.com")
driver.maximize_window()
driver.implicitly_wait(15)
links=driver.find_elements(By.TAG_NAME,'a')
print(links)
print(len(links))
for i in links:
    print(i.text)

driver.quit()
'''

'''
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys("watches")
driver.find_element(By.ID,'nav-search-submit-button').click()

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
driver.quit()
'''

'''
# get_attribute
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(15)
ele = driver.find_elements(By.XPATH,'//a[@class="gb_A"]')
print(ele.get_attribute('aria-label'))
'''

'''
driver.get("https://amazon.in/")
driver.implicitly_wait(10)
ele = driver.find_elements(By.XPATH,'//div[@id="nav-main"]//a')
for i in ele:
    if i.text != "":
        print(i.text," : ",i.get_attribute("href"))
driver.quit()
'''

'''
is_displayed()
Checks whether the element is visible on the webpage or not.

is_enabled()
Checks whether the element is enabled (clickable/usable)

is_selected()
Checks whether the element is selected or not
Works for:
Checkbox ✅
Radio button 🔘
Dropdown (selected option)

'''


# driver.get("https://facebook.com")
# driver.maximize_window()
# driver.implicitly_wait(15)
# ele=driver.find_element(By.XPATH,'//input[@type="text"]')
# print(ele.is_displayed())
# print(ele.is_enabled())


# driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
# driver.maximize_window()
# driver.implicitly_wait(15)
# ele=driver.find_element(By.XPATH,'//button[text()="Register now"]')
# print(ele.is_displayed())
# print(ele.is_enabled())


# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.maximize_window()
# driver.implicitly_wait(15)
#
# btn1 = driver.find_element(By.XPATH,'(//input[@type="checkbox"])[1]')
# print(btn1.is_selected())
#
# btn2 = driver.find_element(By.XPATH,'(//input[@type="checkbox"])[2]')
# print(btn2.is_selected())
#
# # driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shoes")
#
# driver.quit()

# driver.get("https://demoqa.com/automation-practice-form")
# driver.maximize_window()
# driver.implicitly_wait(15)
# driver.find_element(By.ID, "firstName").send_keys("Nehal")
# driver.find_element(By.ID, "lastName").send_keys("Agarwal")
# driver.find_element(By.ID, "userEmail").send_keys("nehal@gmail.com")
# driver.find_element(By.XPATH, "//label[text()='Female']").click()
# driver.find_element(By.ID, "userNumber").send_keys("9876543210")
# dob = driver.find_element(By.ID, "dateOfBirthInput")
# dob.send_keys(Keys.CONTROL + "a")
# dob.send_keys("18 Jan 2004")
# dob.send_keys(Keys.ENTER)
# driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
# driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)
# driver.find_element(By.XPATH, "//label[text()='Sports']").click()
# driver.find_element(By.ID, "currentAddress").send_keys("Jaipur, Rajasthan")
# driver.execute_script("window.scrollBy(0,500)")
# driver.find_element(By.ID, "submit").click()
# driver.quit()
# driver.quit()


# from time import sleep
#
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://demowebshop.tricentis.com/register")
# driver.maximize_window()
# driver.implicitly_wait(15)
# driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
# driver.find_element(By.XPATH, "//input[@id= 'FirstName']").send_keys("Nehal")
# driver.find_element(By.XPATH, "//input[@id= 'LastName']").send_keys(" Agarwal")
# driver.find_element(By.XPATH, "//input[@id= 'Email']").send_keys("xyz@gmail.com")
# driver.find_element(By.XPATH, "//input[@id= 'Password']").send_keys("1234567890")
# driver.find_element(By.XPATH, "//input[@id= 'ConfirmPassword']").send_keys("1234567890")
# driver.find_element(By.ID, "register-button").click()
# driver.close()


from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.ID, "singleFileInput").send_keys(r"D:\New folder (3)\images.jpg")


# is_displayed() and is_enabled() method
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(5)
ele = driver.find_element(By.XPATH,"//span[text()='Log in']")
print("Displayed:",ele.is_displayed())
print("Enabled:",ele.is_enabled())
driver.close() """

# 2
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium=cpc&utm_campaign=Brand_Login_Register&gclsrc=aw.ds&gad_source=1&gad_campaignid=292348446&gbraid=0AAAAADLp3cHQGK0hvfh6zjohfDHagIT1L&gclid=EAIaIQobChMIjM_VsbSrkwMVWco8Ah3GhwtJEAAYASAAEgLL9vD_BwE")
driver.maximize_window()
driver.implicitly_wait(5)
ele = driver.find_element(By.XPATH,"//button[@type='submit']")
print("Displayed:",ele.is_displayed())
print("Enabled:",ele.is_enabled())
driver.close() """

# is_selected method
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()
driver.implicitly_wait(5)
ele1 = driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
ele2 = driver.find_element(By.XPATH,"//input[@type='checkbox'][2]")
print("Checkbox1 is selected:",ele1.is_selected())
print("Checkbox2 is selected:",ele2.is_selected())
driver.close() """

# filling a form
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/automation-practice-form")
driver.find_element(By.ID,"firstName").send_keys("Kriti")
driver.find_element(By.ID,"lastName").send_keys("Jain")
driver.find_element(By.ID,"userEmail").send_keys("kritijain617@gmail.com")
driver.find_element(By.ID,"gender-radio-2").click()
driver.find_element(By.ID,"userNumber").send_keys("1234567890")
driver.find_element(By.ID,"dateOfBirthInput").click()
driver.find_element(By.XPATH,"//div[text()='25']").click()
driver.find_element(By.ID,"hobbies-checkbox-2").click()
# upload files in forms
driver.find_element(By.ID,"uploadPicture").send_keys(r"C:\Desktop\capegemini\Kriti Jain Photo.png") #if path has space then use r before path
driver.find_element(By.ID,"currentAddress").send_keys("JECRC University, Jaipur")
driver.quit()