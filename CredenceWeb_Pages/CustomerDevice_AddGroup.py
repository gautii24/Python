class DeviceAddGroup:

    def __init__(self, driver):
        self.driver=driver
        self.enterGroupName.xpath = "//input[@name='nameGroupName']"
        self.groupPageSearch.xpath = "//input[@name='search']"
        self.groupPagePageDrop.xpath = "//select[@id='formSelectSizePerPage']"
        self.groupTableSerialNumber.xpath = "//th[text()='Serial Number']"
        self.groupTableIMEI.xpath = "//th[text()='IMEI']"
        self.groupTableMacAddress.xpath = "//th[text()='MAC Address']"
        self.groupTableDeviceType.xpath = "//th[text()='Device Type']"
        self.groupTableGroupName.xpath = "//th[text()='Group Name']"
        self.groupTableStatus.xpath = "//th[text()='Status']"
        self.groupPageHeader.xpath = "//div[text()='Create Group']"
        self.tableSerialContent.xpath = "//tr/td[2]|//th[text()='Serial Number']"
        self.tableIMEIContent.xpath = "//tr/td[3]|//th[text()='IMEI']"
        self.tableMacAddressContent.xapth = "//tr/td[4]|//th[text()='MAC Address']"
        self.tableDeviceTypeContent.xpath = "//tr/td[5]|//th[text()='Device Type']"
        self.tableGroupNameContent.xpath = "//tr/td[6]|//th[text()='Group Name']"
        self.tableStatusContent.xpath = "//tr/td[7]|//th[text()='Status']"
        self.GroupPagePreviousPage.xpath = "//a[text()='Previous Page']"
        self.GroupPageNextPage.xapth = "//a[text()='Next Page']"

    def EnterGroupName(self, groupName):
        self.driver.find_element_by_xpath(self.enterGroupName.xpath).send_keys(groupName)

    def SearchGroupPage(self, searchgroupName):
        self.driver.find_element_by_xpath(self.groupPageSearch.xpath).send_keys(searchgroupName)

    def GroupPageDropDown(self):
        self.driver.find_element_by_xpath(self.groupPagePageDrop.xpath).click()

    def ClickGroupTableSerialNumber(self):
        self.driver.find_element_by_xpath(self.groupTableSerialNumber.xpath).click()

    def ClickGroupTableIMEI(self):
        self.driver.find_element_by_xpath(self.groupTableIMEI.xpath).click()

    def ClickGroupTableMacAddress(self):
        self.driver.find_element_by_xpath(self.groupTableMacAddress.xpath).click()

    def ClickGroupTableDeviceType(self):
        self.driver.find_element_by_xpath(self.groupTableDeviceType.xpath).click()

    def ClickGroupTableGroupName(self):
        self.driver.find_element_by_xpath(self.groupTableGroupName.xpath).click()

    def ClickGroupTableStatus(self):
        self.driver.find_element_by_xpath(self.groupTableStatus.xpath).click()

    def CheckHeaderPage(self):
        self.driver.find_element_by_xpath(self.groupPageHeader.xpath).is_displayed()

