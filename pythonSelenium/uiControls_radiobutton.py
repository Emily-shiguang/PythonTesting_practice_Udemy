import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

radiobuttons[1].click()  # if the order will not change
assert radiobuttons[1].is_selected()

# for radiobutton in radiobuttons:
#     if radiobutton.get_attribute("value") == "radio2":
#         radiobutton.click()
#         assert radiobutton.is_selected()
#         break

time.sleep(2)
driver.quit()