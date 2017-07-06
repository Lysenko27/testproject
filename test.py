import unittest
from selenium import webdriver
from helper import wait_until, mail_indexes_of
from pages.compose_mail_page import ComposeMailPage
from pages.login_page import LoginPage
from pages.mailer_main_page import MailerMainPage
from shortcuts import send_email
import datetime


class TestMail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.mailer_page = MailerMainPage(self.driver)
        self.current_page = ComposeMailPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        self.login_page.authorization()


    def test_mail_send_and_delete(self):
        subject = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        send_email(self.driver,self.mailer_page,self.current_page,subject)
         # assert that we have exactly one mail
        self.mailer_page.delete_selected(subject)
         # should be zero emails by now

    def test_move_folder(self):
        subject = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        send_email(self.driver,self.mailer_page,self.current_page,subject)
        self.mailer_page.move_email('Спам',subject)
        self.mailer_page.go_to_folder('#spam',subject)
        wait_until(lambda: len(mail_indexes_of(subject, self.mailer_page.reload_and_fetch_mail())), 10, 1)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMail)
    unittest.TextTestRunner(verbosity=2).run(suite)
