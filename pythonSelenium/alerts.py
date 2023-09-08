import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "BXG"
service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert1 = driver.switch_to.alert
alertText1 = alert1.text
print(alertText1)
time.sleep(2)
alert1.accept()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alert2 = driver.switch_to.alert
alertText2 = alert2.text
print(alertText2)
assert name in alertText2
time.sleep(2)
alert2.dismiss()
# alert2.accept()

driver.quit()