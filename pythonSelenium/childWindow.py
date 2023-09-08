import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windows_handles = driver.window_handles
driver.switch_to.window(windows_handles[1])
print("Child window: ", driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windows_handles[0])
print("Parent window: ", driver.find_element(By.TAG_NAME, "h3").text)
assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"
driver.quit()