from pages.mailer_main_page import *
from pages.compose_mail_page import *

def send_email(driver, recipient, subject, text):
    MailerMainPage(driver).compose_email()
    current_page = ComposeMailPage(driver)
    current_page.send_email(recipient, subject, text)
    driver.get('https://mail.yandex.ru')
