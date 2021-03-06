import pytest

from pageObjects.LoginSignup import LoginSignup
from TestData.LoginSignUpData import LoginSignUpData
from utilities.BaseClass import BaseClass

class Test_Login(BaseClass):


    def test_login(self, getData):
        log = self.getLogger()

        login = LoginSignup(self.driver)

        log.info("Getting Info")

        self.driver.implicitly_wait(50000)
        login.getLoginPopupLink().click()
        log.info("Clicking on the login link to get login popup")
        self.driver.implicitly_wait(30000)
        login.getLoginUserName().click()
        log.info("Clicking on Username Field")
        login.getLoginUserName().send_keys(getData["Email"])
        log.info("Entering Email")
        login.getLoginPassword().click()
        log.info("Clicking on Password Field")
        login.getLoginPassword().send_keys(getData["Password"])
        log.info("Entering Password")
        login.getLoginButton().click()
        log.info("Submitting Login Info")

        self.driver.implicitly_wait(100000)

        loginSucess = login.getLoginicon().is_displayed()

        assert loginSucess

        # if loginSucess == True:
        #     return loginSucess
        # else:
        #     return False



    def test_logout(self):
        log = self.getLogger()
        logout = LoginSignup(self.driver)


        logout.getLoginicon().click()
        log.info("Clicked On Login Icon")
        logout.getLogoutLink().click()
        log.info("Clicked on Logout link")
        self.driver.implicitly_wait(50000)

        logoutSucess = logout.getLoginPopupLink().is_displayed()

        assert logoutSucess




    # @pytest.fixture(params= [("testingbuilder2@yopmail.com", "A@a12345")])
    # def getData(self, request):
    #     return request.param

    # @pytest.fixture(params= [{"Email": "testingbuilder2@yopmail.com", "Password": "A@a12345"}])
    # def getData(self, request):
    #     return request.param

    @pytest.fixture(params= LoginSignUpData.getTestData("TestCase2"))
    def getData(self, request):
        return request.param


#need to implement 2 Data Sets


