class DeviceAddGroup:

    def __init__(self, driver):
        self.driver=driver
        self.enterGroupName.xpath = "//input[@name='nameGroupName']"
        self.addGoupSearch.xpath = "//input[@name='search']"
        self.addGroupsearchTab.xpath = "//select[@id='formSelectSizePerPage']"
        self.allDevices.xpath = "//div[@title='All Devices']"
        self.pageDrop.xpath = "//select[@id='formSelectSizePerPage']"



    def clickAddGroup(self):
        self.driver.find_element_by_xpath(self.addGroupName.xpath).click()

    def clickListView(self):
        self.driver.find_element_by_xpath(self.listView.xpath).click()

    def enterIntoSearchTab(self, searchItem):
        self.driver.find_element_by_xpath(self.searchTab.xpath).send_keys(searchItem)

    def allDevicesCard(self):
        self.driver.find_element_by_xpath(self.allDevices.xpath).click()

    def clickPageViewOption(self):
        self.driver.find_element_by_xpath(self.pageDrop.xpath).click()