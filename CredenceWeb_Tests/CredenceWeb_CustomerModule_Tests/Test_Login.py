import pytest
from CredenceWeb_SetUp.BaseTest import Test_BaseTest
from CredenceWeb_Utilities.LoginIntoApplication import LoginToApplication
from CredenceWeb_Utilities.ReadFromFile import ReadFromFiles
from CredenceWeb_Pages.WelcomePage import WelcomePage
from CredenceWeb_Pages.CommonPage import CommonPage
class TestLoginCheck(Test_BaseTest):


    def test_checklogin(self, test_base):
        LoginToApplication.loginToApp(self, 1, 0)

    # @pytest.mark.run(order=2)
    # def test_functionalLoginTest(selfself, test_base):

    # def test_loginFunctionalityCheck(self, test_base):
    #
    #     rowCount = ReadFromFiles.countActiveRows(self, 'LoginCredentials')
    #     for i in range(2, rowCount):
    #         username = ReadFromFiles.readFromExcel(self, 'LoginCredentials', i, 0)
    #         password = ReadFromFiles.readFromExcel(self, 'LoginCredentials', i, 1)
    #         welcomePage = WelcomePage(self.driver)
    #         commonPage = CommonPage(self.driver)
    #         welcomePage.enterUserName(username)
    #         welcomePage.enterPassword(password)
    #         welcomePage.clickTermsConditions()
    #         welcomePage.clickSigIn()
    #         notificationElement = self.driver.find_element_by_xpath("//a[text()='Notifications']").is_displayed()
    #         expectedResult = True
    #         if NotificationElement:
    #             assert nt
    #
    #
    #
    #         i = i + 1







