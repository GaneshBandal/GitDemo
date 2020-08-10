
import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
# Now find the locators which are common for all options
countries=driver.find_element_by_css_selector("li[class='ui-menu-item'] a")
for country in countries:
    if country.text=="India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text)
driver.find_element_by_id("autosuggest").get_attribute('value')
