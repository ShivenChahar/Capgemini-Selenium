'''

Action: click(), send_keys()

Action keys: there called by Keys Class
        ->Syntax = send_keys(Key.ENTER)


Action Chain CLass : it will  create an object then store the object only then it will perform by .perform() only
                ->   Instead of doing one action at a time (like click or type), you can combine actions
        -> 1. Create Object
        -> 2. Store action
        -> 3. Perform it by .perform()
                -> Syntax: actions = ActionChains(driver)
                            actions.click(single).perform()

Scroll -- >1. scroll_to_element
                            -> Syntax: actions.scroll_to_element(element).perform()
           2. scroll_by_amount()
                            -> Syntax: actions.scroll_by_amount(amount).perform()
           3. scroll_from_origin()
                            -> Syntax: actions.scroll_from_origin(origin).perform()
                            example: search_box = driver.find_element(By.ID, "twotabsearchtextbox")
                                    origin = ScrollOrigin.from_element(search_box)
                                    actions.scroll_from_origin(origin, 0, 1300).perform()

Hover to the element :
                Syntax -> actions.move_to_element(hover).perform()

Hold an element:
                Syntax -> actions.click_and_hold(hold).perform()

Drag and drop :
                Syntax -> actions.pause(2).drag_and_drop(dra, dop).perform()

## Tab Switching :
Switch to another Tab or Window:
                               1.  to fetch the id of the current window or page -> Current_window_handle
                               2.  to know or fetch all the id of the tab -> window_handles [ give as list of all te address]
                               3.  to switch btw different window  -> switch_to.window(window_id)

'''
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
options=ChromeOptions()
options.add_experimental_option("detach",True)
driver=Chrome(options=options)
# driver.get("https://www.amazon.com")
# driver.maximize_window()
# sleep(2)
# search = driver.find_element(By.ID, 'twotabsearchtextbox')
# search.send_keys("Apple Iphone")
# search.send_keys(Keys.ENTER)
# # driver.find_element(By.ID, 'nav-search-submit-button').click()
# sleep(2)

############################################(Action Controls For Performing Actions Direct on the Web-Page)##################################################

# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(2)
# curr = driver.find_element(By.ID, 'currentAddress')
# curr.send_keys("Jaipur, Rajasthan")
# curr.send_keys(Keys.CONTROL,'a')
# curr.send_keys(Keys.CONTROL,'c')
# sleep(2)
# perm = driver.find_element(By.ID, 'permanentAddress')
# # perm.send_keys(Keys.CONTROL,'a')
# perm.send_keys(Keys.CONTROL,'v')


##########################################(Clicking the elements by Actions Chains)################################################
# driver.get('https://demoqa.com/buttons')
# driver.maximize_window()
# sleep(2)
# # driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]").click()      Traditional Method
# # sleep(2)
# single_click = driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]")
# action = ActionChains(driver)                            # Using the ActionChains to perfrom Different Tasks Easily.
# action.click(single_click).perform()                # .Perform is important because without this our actions are only getting stored in teh element and to perform them it is imp.
# double_click = driver.find_element(By.ID,'doubleClickBtn')
# action.double_click(double_click).perform()                      # Here we use actions and perform Double CLick
# sleep(2)
# right_click = driver.find_element(By.ID,'rightClickBtn')
# action.context_click(right_click).perform()                          # Here we use Context instead Right because when we click Right button we get Context.

##########################################(Scrolling of the Web-Page)###################################################
#############################################(Scroll to the Element)###########################################################
# driver.get("https://www.amazon.in")
# driver.implicitly_wait(10)
# driver.maximize_window()
#
# element = driver.find_element(By.XPATH, '(//img[@class = "product-image"])[2]')
# actions = ActionChains(driver)
# actions.scroll_to_element(element).pause(3).click(element).perform()                         # This is used to Scroll to a element and then clicking the element by the given value.
# # actions.click(element).perform()
# sleep(8)
# driver.quit()

###############################################(Scroll by Amount(By the help of Co-ordinates))#######################################################
# driver.get("https://www.amazon.in")
# driver.implicitly_wait(100)
# driver.maximize_window()
#
# actions = ActionChains(driver)
# # sleep(3)
# actions.pause(2).scroll_by_amount(0,1000).perform()
# actions.pause(2).scroll_by_amount(0,900).perform()
# actions.pause(2).scroll_by_amount(0,900).perform()
# # driver.quit()

#######################################(Scroll by Origin (And we can give any value to the origin))#####################################################

# driver.get("https://www.amazon.in")
# driver.implicitly_wait(100)
# driver.maximize_window()
#
# actions = ActionChains(driver)
# # sleep(3)
# element = driver.find_element(By.XPATH, '(//img[@class = "product-image"])[2]')
# origin = ScrollOrigin.from_element(element)
# actions.pause(2).scroll_from_origin(origin, 0,100).perform()
# sleep(10)
# driver.quit()

##########################################(Holding a value in the Web-Page(Which is dynamically hiding again and again))#######################################################

# driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
# cross = driver.find_element(By.XPATH, '//span[@class="ng-tns-c2785778308-3 icon-cancel"]')
# cross.click()
# driver.implicitly_wait(10)
# driver.maximize_window()
# actions = ActionChains(driver)
# search = driver.find_element(By.ID, "password")
# search.send_keys("asdfghjkl")
# sleep(2)
# eye = driver.find_element(By.XPATH, "//img[@class='ng-star-inserted']")
# actions.click_and_hold(eye).pause(5).release().perform()
#
# sleep(2)
# driver.quit()

############################################(Drag & Drop (By Picking the Dragger to the Drop))#######################################################

# driver.get('https://demoqa.com/droppable')
# driver.implicitly_wait(10)
# driver.maximize_window()
# drag = driver.find_element(By.ID, 'draggable')
# drop = driver.find_element(By.ID, 'droppable')
# actions = ActionChains(driver)
# actions.pause(3).drag_and_drop(drag, drop).perform()
#
# sleep(5)
# driver.quit()

##########################################(Tab & Window Switching)##########################################

driver.get('https://google.com')
sleep(5)
actions = ActionChains(driver)
# Manually opening 3 tabs.
driver.maximize_window()
print(driver.title)
print(driver.current_window_handle)
driver.switch_to.new_window()
driver.get('https://amazon.in/')
print(driver.title)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.PARTIAL_LINK_TEXT,'About').click()

sleep(5)
driver.quit()