from selenium import webdriver
import pytest
from CredenceWeb_Utilities.ReadFromFile import ReadFromFiles


class Test_BaseTest:

    @pytest.yield_fixture()
    def test_base(self):
        self.driver = webdriver.Chrome(executable_path="D:/FinalFrameWork/BrowserDrivers/chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://devconnect.credenceid.com/")
        yield
        self.driver.quit()

    # def pytest_addoption(parser):
    #     parser.addoption("--browser", help="Need to enter the browser name on which TestSuite should run")
    #     parser.addoption("--platform", help="Need to enter the OS name on which TestSuite should run")

    # @pytest.fixture()
    # def browser(request):
    #     return request.BaseTest.getoption("--browser")
    #
    # @pytest.fixture()
    # def platform(request):
    #     return request.BaseTest.getoption("--platform")




