from CredenceWeb_SetUp.BaseTest import Test_BaseTest
from CredenceWeb_Utilities.ReadFromFile import ReadFromFiles
from CredenceWeb_Pages.WelcomePage import WelcomePage
from CredenceWeb_Utilities.CustomSeleniumDriver import CustomDriver
from CredenceWeb_Pages.CommonElementsPage import CommonElementsPage
from CredenceWeb_Pages.CommonElementsPage import CommonElementsPage
import time


class TestLoginCheck(Test_BaseTest):



    #Check Login Functionality with Valid Credentials
    def test_valid_loginFunctionalityCheck(self, test_base):
        welcomePage = WelcomePage(self.driver)
        commonElements = CommonElementsPage(self.driver)
        rowMax = ReadFromFiles.countActiveRows(self, 'Valid_LoginCredentials')
        for i in range(2, rowMax+1):
            userName = ReadFromFiles.readFromExcel(self, 'Valid_LoginCredentials', i, 1)
            password = ReadFromFiles.readFromExcel(self, 'Valid_LoginCredentials', i, 2)
            welcomePage.loginIntoApplication(userName, password)
            commonElements.clickProfileArrow()
            commonElements.clickSignOut()

    def test_Invalid_loginFunctionalityCheck(self, test_base):
        welcomePage = WelcomePage(self.driver)
        rowCount = ReadFromFiles.countActiveRows(self, 'InValid_LoginCredentials')
        print(rowCount)
        for i in range(2, rowCount+1):
            userName = ReadFromFiles.readFromExcel(self, 'InValid_LoginCredentials', i, 1)
            password = ReadFromFiles.readFromExcel(self, 'InValid_LoginCredentials', i, 2)
            welcomePage.loginIntoApplication(userName, password)
            time.sleep(3)
            welcomePage.waitdisplayerrorMessage()












