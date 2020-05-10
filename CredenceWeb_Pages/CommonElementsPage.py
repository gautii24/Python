from CredenceWeb_Utilities.CustomSeleniumDriver import CustomDriver
from selenium.webdriver.common.by import By

class CommonElementsPage(CustomDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators of Login Page

    _commonElements_profileArrow = "//button[@class='profile-dropdown dropdown-toggle btn btn-success']"
    _commonElements_profileOption = "//a[text()='Profile']"
    _commonElements_signOut = "//a[text()='Sign Out']"

    # Elements of Login Page

    def getProfileArrow(self):
        return self.driver.find_element(By.XPATH, self._commonElements_profileArrow)

    def getProfileOption(self):
        return self.driver.find_element(By.XPATH, self._commonElements_profileOption)

    def getSignOut(self):
        return self.driver.find_element(By.XPATH, self._commonElements_signOut)

    # Generic methods of Login Page

    def clickProfileArrow(self):
        self.elementClick(self._commonElements_profileArrow, locatorType="xpath")

    def clickProfileOption(self):
        self.elementClick(self._commonElements_profileOption, locatorType="xpath")

    def clickSignOut(self):
        self.elementClick(self._commonElements_signOut, locatorType="xpath")

