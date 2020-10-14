from selenium import webdriver


driver = webdriver.Chrome(executable_path="/Users/Sulabh/PycharmProjects/PythonSelfFramework/chromedriver")
driver.get("http://3.6.127.100:8001/")
driver.maximize_window()

driver.implicitly_wait(3000)

driver.find_element_by_link_text("Sign Up").click()
#driver.find_element_by_xpath("//*[@id = 'agent']").click()
driver.find_element_by_xpath("//*[@id = 'signup-name']").click()
driver.find_element_by_xpath("//*[@id = 'signup-name']").send_keys("Auto Test Owner11")
driver.find_element_by_xpath("//*[@id = 'signup-email']").click()
driver.find_element_by_xpath("//*[@id = 'signup-email']").send_keys("autotestowner11@yopmail.com")
driver.find_element_by_xpath("//*[@id = 'signup-password']").click()
driver.find_element_by_xpath("//*[@id = 'signup-password']").send_keys("A@a12345")
driver.find_element_by_xpath("//*[@id = 'signup-terms']").click()
driver.find_element_by_xpath("//*[@id = 'signup-country-code']").click()
driver.find_element_by_xpath("//*[@id = 'signup-country-code']").clear()
driver.find_element_by_xpath("//*[@id = 'signup-country-code']").send_keys("+91")
driver.find_element_by_xpath("//*[@id = 'signup-mobile-no']").click()
driver.find_element_by_xpath("//*[@id = 'signup-mobile-no']").send_keys("81211244141")
driver.find_element_by_xpath("(//*[@class = 'submitBtn'])[2]").click()


sucessText = driver.find_element_by_xpath("(//*[@class = 'submitBtn'])[2]").is_enabled()
print(sucessText)
assert (sucessText)

driver.refresh()


driver.find_element_by_link_text("Login").click()
driver.find_element_by_id("login-username").click()
driver.find_element_by_id("login-username").send_keys("testingbuilder2@yopmail.com")
driver.find_element_by_id("login-password").click()
driver.find_element_by_id("login-password").send_keys("A@a12345")
driver.find_element_by_id("login-button").click()

loginSucess = driver.find_element_by_xpath("//*[@id ='welcome']/img").is_displayed()

assert (loginSucess)

driver.refresh()