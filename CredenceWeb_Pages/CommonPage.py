class CommonPage():

    def __init__(self, driver):
        self.driver = driver;
        self.arrowbutton_xpath = "//button[@class='profile-dropdown dropdown-toggle btn btn-success']"
        self.signoutOption_xpath = "//a[text()='Sign Out']"
        self.deviceMenuLeft.xpath = "(//a[text()='Devices'])[1]"

    def clickProfileArrow(self):
        self.driver.find_element_by_xpath(self.arrowbutton_xpath).click()

    def clickSignOut(self):
        self.driver.find_element_by_xpath(self.signoutOption_xpath).click()

    def clickdeviceMenu(self):
        self.driver.find_element_by_xpath(self.deviceMenuLeft.xpath).click()

