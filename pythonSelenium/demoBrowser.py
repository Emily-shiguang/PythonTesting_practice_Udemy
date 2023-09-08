from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# -- Chrome
# # service_obj = Service("/Users/emily/Downloads/chromedriver_mac64")
service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# -- Firefox
# service_obj = Service("/usr/local/bin/geckodriver")
# driver = webdriver.Firefox(service=service_obj)

# -- Edge
# service_obj = Service("/usr/local/bin/msedgedriver")
# driver = webdriver.Edge(service=service_obj)


driver.maximize_window()
driver.get("https://www.davidjones.com/")
print(driver.title)
print(driver.current_url)  # when start with automatic first make sure we land on the proper URL before continue testing
driver.get("https://www.myer.com")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()