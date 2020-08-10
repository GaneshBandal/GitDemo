from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_id("exampleCheck1").click()
#driver.find_element_by_css_selector("input[name='name]").send_keys("Rahul")
dropdown=Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)


driver.find_element_by_name("email").send_keys("Shetty")
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)

driver.get("https://login.salesforce.com/")

# driver.find_element_by_xpath("//a[text()='Cancel']").click()
# print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text())
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)


