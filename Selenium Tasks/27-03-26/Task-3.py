from time import sleep
from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://demowebshop.tricentis.com/login')
driver.implicitly_wait(10)
actions = ActionChains(driver)
actions.pause(3).scroll_by_amount(0, 1000).perform()
driver.find_element(By.XPATH, '//a[text()="Facebook"]').click()
sleep(5)
# driver.find_element(By.XPATH, '(//div[@class="x78zum5 xdt5ytf xh8yej3"])[1]').send_keys('SHIVEN@gmail.com')
# driver.find_element(By.XPATH, '(//span[@class="x1jchvi3 x1fcty0u x132q4wb x193iq5w x1al4vs7 x72wyj2 xmper1u x1lliihq x11dcrhx xzwoauc x6ikm8r x10wlt62 x47corl x10l6tqk xlyipyv xoyzfg9 xhb22t3 x11xpdln x1r7x56h xuxw1ft"])[2]').send_keys('**********')
driver.find_element(By.XPATH, '(//span[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84"])[2]').click()