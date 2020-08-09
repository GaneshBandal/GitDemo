from selenium import webdriver


# browser exposes an executable file, through selenium
# you need to invoke that executable file which is given by browser team which is responsible to
#invoke the actual browser # Through selenium test we need to invoke the executable file
#which will then invoke the actual browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
#get method to hit url on browser
driver.get("https://rahulshettyacademy.com")
print(driver.title)

# verify whether we have landed in the correct url or not
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
#browser should get close automatically
driver.close()  # only current window will be closed and driver.quit() all the window will be closed