import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
for result in results:
    actualList.append(result.find_element(By.CSS_SELECTOR, "h4[class='product-name']").text)
    result.find_element(By.XPATH, "div/button").click()  # chaining of web elements
print(actualList)
assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print("Sum: ", sum)
totolAmt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print("Totol amount: ", totolAmt)
assert sum == totolAmt
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)

discountedAmt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print("Discounted Amount: ", discountedAmt)
assert discountedAmt < totolAmt

time.sleep(2)
driver.quit()