from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Rahul")
driver.find_element_by_id("exampleCheck1").click()
#driver.find_element_by_css_selector("input[name='name]").send_keys("Rahul")
driver.find_element_by_name("email").send_keys("Shetty")
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)



