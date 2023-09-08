import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
time.sleep(1)
# collect all veg names -> BrowserSortedVegList
BrowserSortedVegList = []
vegElements = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
for veg in vegElements:
    BrowserSortedVegList.append(veg.text)
# sort this BrowserSortedVegList -> newSortedVegList
print("Before sorted: ", BrowserSortedVegList)
orignialBroswerSortedVegList = BrowserSortedVegList.copy()  # copy a list
BrowserSortedVegList.sort()  # after sort(), the values update into BrowserSortedVegList
print("After sorted: ", BrowserSortedVegList)
# BrowserSortedVegList == newSortedVegList
assert BrowserSortedVegList == orignialBroswerSortedVegList

driver.quit()

