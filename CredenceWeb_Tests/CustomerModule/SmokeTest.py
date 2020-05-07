from allure_commons.types import AttachmentType
from CredenceWeb_Pages.CommonPage import CommonPage
from CredenceWeb_Pages.WelcomePage import WelcomePage
import pytest
from CredenceWeb_BaseTest.BaseTest import Test_BaseTest
import allure_commons
import allure_pytest
import allure


class TestLoginCheck(Test_BaseTest):

    allure.description("Checking Login Functionality")
    allure.severity(severity_level="HIGH")
    def test_checklogin(self, test_base):
        driver=self.driver
        welcomePage = WelcomePage(driver)
        commonpage = CommonPage(driver)
        welcomePage.enterUserName("credencetestc@gmail.com")
        allure.step("Entered Username")
        allure.attach(self.driver.get_screenshot_as_png(), name="Credentials Added", attachment_type=AttachmentType.PNG)
        allure.step("Screenshot Captured")
        welcomePage.enterPassword("India@12345")
        allure.step("Entered Password")
        welcomePage.clickTermsConditions()
        welcomePage.clickSigIn()
        commonpage.clickProfileArrow()
        commonpage.clickSignOut()

    def test_printlogin(self, test_base):
        print("Login")

