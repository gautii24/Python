import pytest
from CredenceWeb_BaseTest.BaseTest import Test_BaseTest
from CredenceWeb_Utilities.LoginIntoApplication import LoginToApplication


class TestLoginCheck(Test_BaseTest):

    def test_checklogin(self, test_base):
        LoginToApplication.loginToApp(self, 1, 0)






