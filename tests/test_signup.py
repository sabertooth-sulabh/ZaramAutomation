import pytest

from pageObjects.LoginSignup import LoginSignup
from utilities.BaseClass import BaseClass
from TestData.LoginSignUpData import LoginSignUpData

class Test_SignUp(BaseClass):

    def test_signup(self, getData):
        log = self.getLogger()
        signup = LoginSignup(self.driver)

        signup.getSignUpPopupLink().click()
        log.info("Clicked on Sigup Popup")
        self.driver.implicitly_wait(50000)
        signup.getSignUpName().click()
        log.info("Clicked on Name Field")
        signup.getSignUpName().send_keys(getData["Name"])
        log.info("Entered Sigup Name")
        signup.getSignUpEmail().click()
        log.info("Clicked on Email Field")
        signup.getSignUpEmail().send_keys(getData["Email"])
        log.info("Entered  Email")
        signup.getSignUpPassword().click()
        log.info("Clicked on Password Field")
        signup.getSignUpPassword().send_keys(getData["Password"])
        log.info("Entered Password")
        signup.getSignUpTerms().click()
        log.info("Clicked on Sigup Terms")
        signup.getSignUpCC().click()
        log.info("Clicked on Country Code Filed")
        signup.getSignUpCC().clear()
        log.info("Cleared Country Code Filed")
        signup.getSignUpCC().send_keys(getData["CC"])
        log.info("Entered Country Code")
        signup.getSignUpMobNo().click()
        log.info("Clicked on Phone No. Filed")
        signup.getSignUpMobNo().send_keys(getData["Phone No"])
        log.info("Entered Phone No.")
        signup.getSignUpSubmitBtn().click()
        log.info("Clicked on Sigup Button")

        sucessText = signup.getSignUpSubmitBtn().is_enabled()
        print(sucessText)
        assert (sucessText)




    @pytest.fixture(params=LoginSignUpData.getTestData("TestCase3"))
    def getData(self, request):
        return request.param


