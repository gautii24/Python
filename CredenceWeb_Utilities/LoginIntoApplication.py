from CredenceWeb_Utilities.ReadFromFile import ReadFromFiles
from CredenceWeb_Pages.WelcomePage import WelcomePage
from CredenceWeb_Pages.CommonPage import CommonPage

class LoginToApplication:

    def __init__(self, driver):
        self.driver = driver

    def loginToApp(self, rowNum, columnNum):
        username = ReadFromFiles.readFromExcel(self, 'LoginCredentials', rowNum, columnNum)
        password = ReadFromFiles.readFromExcel(self, 'LoginCredentials', rowNum, columnNum+1)
        welcomePage = WelcomePage(self.driver)
        welcomePage.enterUserName(username)
        welcomePage.enterPassword(password)
        welcomePage.clickTermsConditions()
        welcomePage.clickSigIn()



