import datetime

from helper import get_random_text_and_number
from pages.mailer_main_page import *
from pages.compose_mail_page import *

def send_email(driver, recipient='rocketbank-fan@yandex.ru', subject=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"), text=get_random_text_and_number()):
    MailerMainPage(driver).compose_email()
    current_page = ComposeMailPage(driver)
    current_page.send_email(recipient, subject, text)
    driver.get('https://mail.yandex.ru')
