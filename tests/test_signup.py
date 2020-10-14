from pageObjects.LoginSignup import LoginSignup
from utilities.BaseClass import BaseClass

class Test_SignUp(BaseClass):

    def test_signup(self):

        signup = LoginSignup(self.driver)

        signup.getSignUpPopupLink().click()
        self.driver.implicitly_wait(50000)
        # driver.find_element_by_xpath("//*[@id = 'agent']").click()
        signup.getSignUpName().click()
        signup.getSignUpName().send_keys("Auto Test Owner5")
        signup.getSignUpEmail().click()
        signup.getSignUpEmail().send_keys("autotestowner5@yopmail.com")
        signup.getSignUpPassword().click()
        signup.getSignUpPassword().send_keys("A@a12345")
        signup.getSignUpTerms().click()
        signup.getSignUpCC().click()
        signup.getSignUpCC().clear()
        signup.getSignUpCC().send_keys("+91")
        signup.getSignUpMobNo().click()
        signup.getSignUpMobNo().send_keys("8121244141")
        signup.getSignUpSubmitBtn().click()

        sucessText = signup.getSignUpSubmitBtn().is_enabled()
        print(sucessText)
        assert (sucessText)








