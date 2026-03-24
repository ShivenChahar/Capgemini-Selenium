from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
options=ChromeOptions()
options.add_argument("--disable-notifications")                            # It is used to disable some of the Unwanted Options.
options.add_experimental_option("prefs",{"safebrowsing.enabled":True})     # It is used for some web-sites which give error in normal browsing
options.add_experimental_option("detach",True)
driver=Chrome(options=options)

##########################################(iFrames Switching and Input)######################################
# driver.get("http://127.0.0.1:5500/Frames_Selenium(Page-1).html")
# sleep(2)
# driver.find_element(By.ID, "input").send_keys("Wallah")
# ######---------Here we have to first Switch to the req. Page and then we can access that Page.
# ######---------There are two attributes in Switching (1. Using Index),(2. Using Name), (3. Using Web-Element)
# driver.switch_to.frame('name1')             # This is the switch by using Name
# driver.switch_to.frame(0)                   # This is the switching by using index (Here we used 0 because this is the first page in action for the main page)
# driver.find_element(By.ID, "input2").send_keys("habi")
# driver.switch_to.frame('name2')
# driver.switch_to.frame(0)                   # In page 3 we again used page 0 because currently we are on Page 2 and approaching from this will need 0.
# driver.find_element(By.ID, "input3").send_keys("biii")

##############################################(Task)##################################################
# driver.get('https://x.com/')
# driver.switch_to.frame(0)
# driver.find_element(By.CLASS_NAME,'nsm7Bb-HzV7m-LgbsSe-BPrWId').click()

##############################################(Task)###################################################
# driver.get('https://www.zomato.com/chennai/restaurants/')
# driver.find_element(By.XPATH, "//a[@class='sc-3o0n99-5 jqszCs']").click()
# sleep(3)
# driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="auth-login-ui"]'))
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Sign in with Google Button']"))
# driver.find_element(By.XPATH, "//span[text()='Sign in with Google']").click()
# sleep(7)
# driver.quit()
############################################(Going Back from Child to the Parent iFrame)#######################################

# driver.get("http://127.0.0.1:5500/Frames_Selenium(Page-1).html")
# sleep(2)
# driver.find_element(By.ID, "input").send_keys("Wallah")
# driver.switch_to.frame('name1')             # This is the switch by using Name
# # driver.switch_to.frame(0)                   # This is the switching by using index (Here we used 0 because this is the first page in action for the main page)
# driver.find_element(By.ID, "input2").send_keys("habi")
# driver.switch_to.frame('name2')
# # driver.switch_to.frame(0)                   # In page 3 we again used page 0 because currently we are on Page 2 and approaching from this will need 0.
# driver.find_element(By.ID, "input3").send_keys("biii")
# # driver.switch_to.parent_frame()             # This is used to go back to the recent parent of the child
# driver.switch_to.default_content()           # This is used to go back to the main default parent.
# sleep(3)
#
# # driver.find_element(By.ID, "input2").send_keys("Wallah Habibii I am Back")          # For changing something in the recent parent
# driver.find_element(By.ID, "input").send_keys("  Wallah")                             # For changing something in the default parent

###############################################(Alert & Pop-Up's)#######################################################

# driver.get("https://testautomationpractice.blogspot.com/#")
# sleep(2)
# driver.maximize_window()
#---------------------I---------Simple ALert---------------
# driver.find_element(By.ID, 'alertBtn').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
#-------------------II-------Confirmation Alert-------------------
# driver.find_element(By.ID, 'confirmBtn').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.accept()                # For Accepting
# # alert.dismiss()             # For Cancelling
#-----------------III--------Prompt Alert-----------------------
# driver.find_element(By.ID, 'promptBtn').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.send_keys("Hello")
# alert.accept()

#################################################(Upload & Download)#########################################
# driver.get("https://demoqa.com/upload-download")
# driver.find_element(By.ID,'uploadFile').send_keys(r"C:\Users\shive\OneDrive\Desktop\Report Acknowledgement page - SUM.docx")
# sleep(2)
# driver.find_element(By.ID,'downloadButton').click()

###############################################(Task)(In this we have to enable a chrome option which will enable the safe-browsing)######################################################
driver.get("https://www.python.org/downloads/")
# options.add_experimental_option("prefs",{"safebrowsing.enabled":True})
sleep(2)
driver.find_element(By.XPATH,'(//a[@href="https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe"])[2]').click()