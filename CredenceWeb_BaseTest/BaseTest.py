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






