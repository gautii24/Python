from selenium.webdriver.common.by import By
from CredenceWeb_Utilities.CustomSeleniumDriver import CustomDriver



class WelcomePage(CustomDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators of Login Page

    _login_usernameField = "//input[@id='formBasicEmail']"
    _login_passwordField = "//input[@id='formBasicPassword']"
    _login_AcceptChbx = "//input[@id='formBasicAccept']"
    _login_signInBtn = "//button[@class='btn btn-default sign-in-btn btn-nocolorbg btn btn-primary']"
    _login_errorMessage = "//div[contains(text(),'Wrong email')]"

    #Elements of Login Page

    def getloginUsername(self):
        return self.driver.find_element(By.XPATH, self._login_usernameField)

    def getloginPassword(self):
        return self.driver.find_element(By.XPATH, self._login_passwordField)

    def getAcceptConditionsChkbx(self):
        return self.driver.find_element(By.XPATH, self._login_AcceptChbx)

    def getSignInButton(self):
        return self.driver.find_element(By.XPATH, self._login_signInBtn)

    def getSignErrorMessage(self):
        return self.driver.find_element(By.XPATH, self._login_errorMessage)


    #Generic methods of Login Page

    def enterUsername(self, username):
        self.elementClear(self._login_usernameField, locatorType="xpath")
        self.sendKeys(username, self._login_usernameField, locatorType="xpath")

    def enterPassword(self, password):
        self.elementClear(self._login_passwordField, locatorType="xpath")
        self.sendKeys(password, self._login_passwordField, locatorType="xpath")

    def clickAcceptTermsCheckbox(self):
        self.elementClick(self._login_AcceptChbx, locatorType="xpath")

    def clickSignInButton(self):
        self.elementClick(self._login_signInBtn, locatorType="xpath")

    def waitdisplayerrorMessage(self):
        self.waitForElement(self._login_errorMessage, locatorType="xpath", timeout=10)


    def loginIntoApplication(self, username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickAcceptTermsCheckbox()
        self.clickSignInButton()













