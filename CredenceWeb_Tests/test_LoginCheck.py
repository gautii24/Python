from allure_commons.types import AttachmentType

from CredenceWeb_Pages.WelcomePage import WelcomePage
import pytest
from CredenceWeb_BaseTest.BaseTest import Test_BaseTest
import allure_commons
import allure_pytest
import allure


class TestLoginCheck(Test_BaseTest):

    def test_checklogin(self, test_base):
        driver=self.driver
        welcomePage = WelcomePage(driver)
        welcomePage.enterUserName("credencetestc@gmail.com")
        allure.attach(self.driver.get_screenshot_as_png(), name="Credentials Added", attachment_type=AttachmentType.PNG)
        welcomePage.enterPassword("India@12345")
        welcomePage.clickTermsConditions()
        welcomePage.clickSigIn()

    def test_printlogin(self, test_base):
        print("Login")

