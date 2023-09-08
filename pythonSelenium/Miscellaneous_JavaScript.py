import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

"""
driver.execute_script is used to execute JavaScript
window.scrollBy(0, 700); don't forget to add ;
scroll used to scroll the window to the position where you want to operate on element
"""
driver.execute_script("window.scrollBy(0, 700);")
driver.get_screenshot_as_file("screen2.png")
driver.quit()
