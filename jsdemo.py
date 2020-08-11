#js DOM can access any elements on web page just like how selenium does
#selenium have a method to execute javascript code in it

from selenium import webdriver

driver=webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#If I want to get the text inside the editbox, first goal is to enter something in editbox
driver.find_element_by_name("name").send_keys("hello")
#now retrieve the text
print(driver.find_element_by_name("name").text)
#but no data is printed, when browser loads some text, only on that specific text u can do .text to retrieve
#If u enter some input from selenium script and if u r trying to grab the text what u entered is not possible using text method
#there r ways but not text method
# 2ways: selenium have inherited one method from javascript DOM get_attribute
#grab the text inside the textbox and value is the default attribute which will provide entered value
print(driver.find_element_by_name("name").get_attribute("value"))
#selenium has method execute_script which executes javascript commands
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
# if u think selenium object is not able to identify the element, use the DOM


# If u click on shop, grb the object
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
#now click the object using JS Executor
driver.execute_script("arguments[0].click();",shopButton)
#selenium does not support scroll down but javascript knows how to scroll down
#how to handle scrolldown using selenium, so we rely on JS executor
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")



