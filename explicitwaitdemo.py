
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

# tagname.classname
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
#after typing ber, it will take some time to show the results
time.sleep(4)

count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count==3
#Now the next goal is to add all items to the cart, if u r adding one by one is not a good way
#tomorrow if there are 100 products displayed, for every product need to write xpath.click
# so try to get all butons using find elements plural, put it in for loop and iterate and click one by one
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
#now go to added cart items
driver.find_element_by_css_selector("img[alt='Cart']").click()
# now click on the button proceed to checkout
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait=WebDriverWait(driver,5)
wait.until(EC.presence_of_element_located((By.CLASS_NAME,"promocode")))
#Enter promo code to get discount
#test failed, not able to enter promocode
driver.find_element_by_class_name("promocode").send_keys("rahulshettyacademy")
#apply button, for css .classname
driver.find_element_by_css_selector(".promobtn").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.promoinfo")))
print(driver.find_element_by_css_selector("span.promoinfo").text)

