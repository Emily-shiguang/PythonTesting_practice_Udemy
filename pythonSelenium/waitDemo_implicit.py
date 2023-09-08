import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)  # 5 seconds here is max timeout, if element appears in 2 seconds then 3 seconds save
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

search_key = "ber"
driver.find_element(By.XPATH, "//input[@type='search']").send_keys(search_key)
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")  # selenium will not implicitly wait here, if no, just return empty list
count = len(results)
print("The number of search result of {} is {}".format(search_key, count))
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()  # chaining of web elements

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)


time.sleep(2)
driver.quit()