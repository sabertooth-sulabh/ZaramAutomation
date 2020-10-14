from selenium.webdriver.common.by import By


class LoginSignup:

    def __init__(self, driver):
        self.driver = driver


    loginLink = (By.LINK_TEXT, "Login")
    loginUserName = (By.ID, "login-username")
    loginPassword = (By.ID, "login-password")
    loginButton = (By.ID, "login-button")

    def getLoginPopupLink(self):
        return self.driver.find_element(*LoginSignup.loginLink)

    def getLoginUserName(self):
        return self.driver.find_element(*LoginSignup.loginUserName)

    def getLoginPassword(self):
        return self.driver.find_element(*LoginSignup.loginPassword)

    def getLoginButton(self):
        return self.driver.find_element(*LoginSignup.loginButton)


#Signup Form Data Below

    signUpLink = (By.LINK_TEXT, "Sign Up")
    signUpName = (By.XPATH, "//*[@id = 'signup-name']")
    signUpEmail = (By.XPATH, "//*[@id = 'signup-email']")
    signUpPassword = (By.XPATH, "//*[@id = 'signup-password']")
    signUpTerms = (By.XPATH, "//*[@id = 'signup-terms']")
    signUpCC = (By.XPATH, "//*[@id = 'signup-country-code']")
    signMobNo = (By.XPATH, "//*[@id = 'signup-mobile-no']")
    signUpSubmitBtn = (By.XPATH, "(//*[@class = 'submitBtn'])[2]")

    def getSignUpPopupLink(self):
        return self.driver.find_element(*LoginSignup.signUpLink)

    def getSignUpName(self):
        return self.driver.find_element(*LoginSignup.signUpName)

    def getSignUpEmail(self):
        return self.driver.find_element(*LoginSignup.signUpEmail)

    def getSignUpPassword(self):
        return self.driver.find_element(*LoginSignup.signUpPassword)

    def getSignUpTerms(self):
        return self.driver.find_element(*LoginSignup.signUpTerms)

    def getSignUpCC(self):
        return self.driver.find_element(*LoginSignup.signUpCC)

    def getSignUpMobNo(self):
        return self.driver.find_element(*LoginSignup.signMobNo)

    def getSignUpSubmitBtn(self):
        return self.driver.find_element(*LoginSignup.signUpSubmitBtn)



