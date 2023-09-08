from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.davidjones.com/")

# ID, Xpath, CSSSelector, Classname, name, linkText
# driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
# driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
# driver.find_element(By.ID, "exampleCheck1").click()

Sel = driver.find_elements(By.CLASS_NAME, "icon-user-single")
print("Select element is visible: ", Sel[2].is_displayed())
Sel[2].send_keys(Keys.ENTER)
sleep(2)

driver.find_element(By.NAME, "emailaddress").send_keys("hello@gmail.com")
driver.find_element(By.ID, "header-password").send_keys("123456")

checkbox = driver.find_element(By.ID, "header-autologin-existing")
action = ActionChains(driver)
action.move_to_element(checkbox).perform()
action.click(checkbox).perform()
sleep(2)

# XPATH - //tagname[@attribute='value'] -> //button[@type='submit']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='error']").text
print(message)
assert "Sorry" in message

# CSS SELECTOR - tagname[attribute='value'] -> //input[name='shipfirstname']
driver.find_element(By.CSS_SELECTOR, "input[name='shipfirstname']").send_keys("Wang")
sleep(2)
driver.find_element(By.XPATH, "//input[@name='shipfirstname']").clear()

sleep(2)
driver.quit()