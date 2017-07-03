import unittest
import time

from helper import mail_indexes_of
from pages.login_page import LoginPage
from pages.mailer_main_page import *
from shortcuts import *
from selenium import webdriver

class TestMail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(10)
        self.driver.get("https://mail.yandex.ru")
        LoginPage(self.driver).login('rocketbank-fan','qwerty$4')


    def test_move_folder(self):
        self.driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[3]/div/div[2]/div[3]/div[2]/div[5]/div[1]/div/div/div[2]/div/div/div/div/div/a/div/span[1]/span[1]').click()


         # should be zero emails by now

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMail)
    unittest.TextTestRunner(verbosity=2).run(suite)




