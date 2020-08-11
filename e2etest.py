from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
#check for blackberry but it may be anywhere, by looping u can verify the blackberry but
#after that how can we click on add button, first identify the product and then go to add button
# first select the entire product
products=driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    productName= product.find_element_by_xpath("div/h4/a").text
    print(productName)
    if productName=="Blackberry":
        #add item to the cart, checkout logic with product selection
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
#once land on the page,next goal is to select checkout
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

#we r on last page where autosuggestive dropdown is there
#first enter in the editbox
driver.find_element_by_id("country").send_keys("ind")
#after i/p it takes some time to load
#Handling autosuggestive dropdown to select location and confirm order
#wait till the linktext is displayed
wait=WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
#once displayed,below logic
driver.find_element_by_link_text("India").click()
#I agree logic
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()

print(driver.find_element_by_class_name("alert-success").text)

#Taking screenshots using Selenium Python with Assertions
driver.get_screenshot_as_file("screen.png")
#take screenshots only when test failed






