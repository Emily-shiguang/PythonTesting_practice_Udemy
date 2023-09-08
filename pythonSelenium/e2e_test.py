from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(4)

# By.CSS_SELECTOR, "a[href*='shop']']", By.XPATH, "//a[contains(@href, 'shop')]"
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

# chaining
# div[class='card h-100']
# div[class='card h-100'] div h4 a
# div[class='card h-100'] div button

products = driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")
for product in products:
    productName = product.find_element(By.CSS_SELECTOR, "div h4 a").text
    if productName == "Blackberry":
        product.find_element(By.CSS_SELECTOR, "div button").click()
        break

driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
# If SelectorsHub is not available in some companies, we can use Console to validate our XPATH and CSS_SELECTOR
# XPATH $x("//button[@class='btn btn-success']")
# CSS $("button[class='btn btn-success']")

driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ch")
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "China")))
driver.find_element(By.LINK_TEXT, "China").click()
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']").click()
successText = driver.find_element(By.CSS_SELECTOR, "[class='alert alert-success alert-dismissible']").text
assert "Success" in successText
driver.close()