class CustomerDevice:

    def __init__(self, driver):
        self.driver=driver
        self.addGroupName.xpath = "//a[text()='Add Group']"
        self.listView.xpath= "//img[@class='layout-mode-image']"
        self.searchTab.xpath = "//input[@id='search_field']"
        self.allDevices.xpath = "//div[@title='All Devices']"
        self.pageDrop.xpath = "//select[@id='formSelectSizePerPage']"



    def enterPassword(self):
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def clickTermsConditions(self):
        self.driver.find_element_by_xpath(self.clickTerms_xpath).click()

    def clickSigIn(self):
        self.driver.find_element_by_xpath(self.clickloginButton_xpath).click()