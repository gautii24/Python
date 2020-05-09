import pytest
import unittest
from CredenceWeb_SetUp.BaseTest import Test_BaseTest
from CredenceWeb_Utilities.LoginIntoApplication import LoginToApplication
from CredenceWeb_Utilities.ReadFromFile import ReadFromFiles
from CredenceWeb_Pages.WelcomePage import WelcomePage
from CredenceWeb_Pages.CommonPage import CommonPage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLoginCheck(Test_BaseTest):

    def test_valid_loginFunctionalityCheck(self, test_base):

        rowCount = ReadFromFiles.countActiveRows(self, 'Valid_LoginCredentials')
        print(rowCount)
        for i in range(2, rowCount+1):
            username = ReadFromFiles.readFromExcel(self, 'Valid_LoginCredentials', i, 1)
            password = ReadFromFiles.readFromExcel(self, 'Valid_LoginCredentials', i, 2)
            welcomePage = WelcomePage(self.driver)
            commonPage = CommonPage(self.driver)
            welcomePage.enterUserName(username)
            welcomePage.enterPassword(password)
            welcomePage.clickTermsConditions()
            welcomePage.clickSigIn()
            assert welcomePage.profileboxDisplayed() == True
            commonPage.clickProfileArrow()
            commonPage.clickSignOut()
            i = i + 1

    # def test_Invalid_loginFunctionalityCheck(self, test_base):
    #
    #     rowCount = ReadFromFiles.countActiveRows(self, 'InValid_LoginCredentials')
    #     print(rowCount)
    #     for i in range(2, rowCount+1):
    #         username = ReadFromFiles.readFromExcel(self, 'InValid_LoginCredentials', i, 1)
    #         password = ReadFromFiles.readFromExcel(self, 'InValid_LoginCredentials', i, 2)
    #         welcomePage = WelcomePage(self.driver)
    #         commonPage = CommonPage(self.driver)
    #         welcomePage.enterUserName(username)
    #         welcomePage.enterPassword(password)
    #         welcomePage.clickTermsConditions()
    #         welcomePage.clickSigIn()
    #         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Wrong email')]")))
    #         assert welcomePage.errorMessage() == True
    #         i = i + 1










