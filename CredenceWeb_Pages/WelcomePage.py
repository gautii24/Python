

class WelcomePage:

    def __init__(self, driver):
        self.driver = driver;
        self.username_xpath = "//input[@id='formBasicEmail']"
        self.password_xpath = "//input[@id='formBasicPassword']"
        self.clickTerms_xpath = "//input[@id='formBasicAccept']"
        self.clickloginButton_xpath = "//button[@class='btn btn-default sign-in-btn btn-nocolorbg btn btn-primary']"

    def enterUserName(self, username):
        self.driver.find_element_by_xpath(self.username_xpath).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def clickTermsConditions(self):
        self.driver.find_element_by_xpath(self.clickTerms_xpath).click()

    def clickSigIn(self):
        self.driver.find_element_by_xpath(self.clickloginButton_xpath).click()








