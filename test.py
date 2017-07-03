import unittest
from selenium import webdriver
from pages.login_page import *
from shortcuts import *
from helper import *
import datetime


class TestMail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(10)
        self.driver.get("https://mail.yandex.ru")
        LoginPage(self.driver).login('rocketbank-fan','qwerty$4')


    def test_mail_send_and_delete(self):
        mailer_page = MailerMainPage(self.driver)
        subject = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        send_email(self.driver,subject)
        wait_until(len(mail_indexes_of(subject, mailer_page.reload_and_fetch_mail())),5,1)
         # assert that we have exactly one mail
        mailer_page.select_email(mail_indexes_of(subject, mailer_page.reload_and_fetch_mail())[0] + 1)
        mailer_page.delete_selected()
        wait_until(len(mail_indexes_of(subject, mailer_page.reload_and_fetch_mail())),5,0)
         # should be zero emails by now

    def test_move_folder(self):
        mailer_page = MailerMainPage(self.driver)
        subject = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        send_email(self.driver,subject)
        wait_until(len(mail_indexes_of(subject, mailer_page.reload_and_fetch_mail())),5,1)
        mailer_page.select_email(mail_indexes_of(subject, mailer_page.reload_and_fetch_mail())[0] + 1)
        mailer_page.move_email()
        wait_until(len(mail_indexes_of(subject, mailer_page.reload_and_fetch_mail())),5,0)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMail)
    unittest.TextTestRunner(verbosity=2).run(suite)
