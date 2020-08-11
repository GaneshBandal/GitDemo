from selenium import webdriver
driver=webdriver.Chrome("C:\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")

# now click on link click here, locator is linktext
driver.find_element_by_link_text("Click Here").click()
childwindow=driver.window_handles[1]
driver.switch_to.window(childwindow)
# switch to new window and pass the window id of that child window but how to get child window id
#window_handles method will actually get all the windows opened by automation and it will be a list and 0th
#indexrepresents parent window
#now get the text of new window, but opening aa new window will be printed instead of Click Here
print(driver.find_element_by_tag_name("h3").text)
driver.close()
#now get back to parent window
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)

