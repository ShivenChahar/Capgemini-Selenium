# Task 4 : upload single and multiple files
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"name").send_keys("Shiven Chahar")
driver.find_element(By.ID,"singleFileInput").send_keys(r"C:\Users\shive\OneDrive\Pictures\Dog Wallpaper\pexels-marian-havenga-531055927-18664591.jpg")
driver.find_element(By.XPATH,"//button[text()='Upload Single File']").click()
# you can also use multiple send keys or for loop
driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\shive\OneDrive\Pictures\Dog Wallpaper\pexels-jaclou-dl-214226-20523057.jpg","\n",r"C:\Users\shive\OneDrive\Pictures\Dog Wallpaper\pexels-stankevic-12562989.jpg")
driver.find_element(By.XPATH,"//button[text()='Upload Multiple Files']").click()