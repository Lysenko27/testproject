import unittest
from selenium import webdriver
from pages.login_page import *
from shortcuts import *
import time
import datetime

def mail_indexes_of(subject, mail):
    mail_indexes = []
    for i in (range(0,len(mail))):
        if mail[i]['subject'] == subject:
          mail_indexes.append(i)
    return(mail_indexes)

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
        send_email(
          self.driver,
          'rocketbank-fan@yandex.ru',
          subject,
          'content123'
        )
        time.sleep(7)
        mail_on_page = mailer_page.reload_and_fetch_mail()
        self.assertEqual(
          len(mail_indexes_of(subject, mail_on_page)),
          1
        ) # assert that we have exactly one mail
        mailer_page.select_email(mail_indexes_of(subject, mail_on_page)[0] + 1)
        mailer_page.delete_selected()
        time.sleep(5)
        mail_on_page = mailer_page.reload_and_fetch_mail()
        self.assertEqual(
          len(mail_indexes_of(subject, mail_on_page)),
          0
        ) # should be zero emails by now


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMail)
    unittest.TextTestRunner(verbosity=2).run(suite)
