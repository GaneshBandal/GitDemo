
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
#If u want to start browser in maximized mode

chrome_options.add_argument("--start-maximized")
# head mode means browser invoking, how do u tell to ur chrome browser to execute in headless mode
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")


driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#chromeoptions class will set the behaviour of browser while invoking