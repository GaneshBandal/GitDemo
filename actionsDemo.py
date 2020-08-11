from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice")
#Next goal is to mouse over the menuitem called MouseOver
#First create object for ActionsChains class and pass driver object to it
action=ActionChains(driver)
#if we want to move the cursor to the mouseover menuitem, first grab the locator
#move_to_element method move the cursor to the element and it take an argument as webelement
menu=driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
#Now after menu is opened, we have to come down and select the top option
# so the first goal is to move the cursor to top and then click
childMenu=driver.find_element_by_link_text("Top")
action.move_to_element(childMenu).click().perform()

#How to handle double click
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action.double_click(driver.find_element_by_id("double-click")).perform()
# now click on ok but it is javascript popup
alert=driver.switch_to.alert
alert.accept()
#for right click context click is there





