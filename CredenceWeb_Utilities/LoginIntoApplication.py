from CredenceWeb_Utilities.ReadFromFile import ReadFromFiles
from CredenceWeb_Pages.WelcomePage import WelcomePage
from CredenceWeb_Pages.CommonPage import CommonPage
import time

class LoginToApplication:

    def __init__(self, driver):
        self.driver = driver

    def loginToApp(self, rowNum, columnNum):
        username = ReadFromFiles.readFromExcel(self, 'LoginCredentials', rowNum, columnNum)
        password = ReadFromFiles.readFromExcel(self, 'LoginCredentials', rowNum, columnNum+1)
        welcomePage = WelcomePage(self.driver)
        welcomePage.enterUserName(username)
        time.sleep(2)
        welcomePage.enterPassword(password)
        time.sleep(2)
        welcomePage.clickTermsConditions()
        time.sleep(3)
        welcomePage.clickSigIn()





