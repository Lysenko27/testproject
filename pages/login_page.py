from pages.base import Page
class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_xpath = '//input[@name="login"]'
        self.password_xpath = '//input[@name="passwd"]'
        self.submit_xpath = '//button[@type="submit"]'
        self.driver = driver



    def authorization(self, login=None, password=None):
        if login == None or password == None:
            login = self.base_login
            password = self.base_password

        self.driver.get(self.base_url)
        self.driver.find_element_by_xpath(self.login_xpath).send_keys(login)
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.submit_xpath).click()
