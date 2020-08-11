from selenium import webdriver

driver=webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
#pass the argument as frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()
#here the test is failed, so why we are not able to do it through selenium bcoz the entire
#editbox is in frames, selenium has only knowledge on html driver but if there is any frame on it which comes
#on top over browser then by default your driver object not have knowledge about that frames so to chk whether
#the content is in frames or not, tage like frame or iframe or frameset, so first switch to frame to handle that

#here the driver object is not of html,it is switched to frames therefore need to switch to the default content
print(driver.find_element_by_tag_name("h3").text)


