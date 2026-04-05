from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("file:///C:/Users/saumya/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/LocalState/sessions/920A8AEEA9A2496B19EF90D1770213276361D039/transfers/2026-12/E22_Dropdowns.html")
driver.maximize_window()
sleep(2)
dropdown=driver.find_element(By.ID,"state")
option=Select(dropdown)
option.select_by_visible_text("Kerala")
sleep(2)
option.select_by_index(4)
sleep(3)
option.select_by_value("KL")
dropdown=driver.find_element(By.ID,"hobby")
option=Select(dropdown)
option.select_by_visible_text("Scrolling")
option.select_by_index(2)
option.deselect_by_index(2)
option.deselect_by_visible_text("Scrolling")
option.deselect_all()