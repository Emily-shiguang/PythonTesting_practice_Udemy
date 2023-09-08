import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
# action.double_click()  # double click
# action.context_click()  # right click
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()  # remember to use .perform
time.sleep(2)
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# time.sleep(2)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(2)
driver.quit()