class CustomerDevice:

    def __init__(self, driver):
        self.driver=driver
        self.addGroupName.xpath = "//a[text()='Add Group']"
        self.listView.xpath= "//img[@class='layout-mode-image']"
        self.searchTab.xpath = "//input[@id='search_field']"
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