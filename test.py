import unittest
from selenium import webdriver
from pages.login_page import *
from shortcuts import *
from helper import get_random_text_and_number
import datetime


class TestMail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(10)
        self.driver.get("https://mail.yandex.ru")
        LoginPage(self.driver).login('rocketbank-fan','qwerty$4')
        self.mailer_page = MailerMainPage(self.driver)
        self.current_page = ComposeMailPage(self.driver)

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
        wait_until(lambda: len(mail_indexes_of(subject, self.mailer_page.reload_and_fetch_mail())), 6, 1)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMail)
    unittest.TextTestRunner(verbosity=2).run(suite)
