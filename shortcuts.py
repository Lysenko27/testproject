from helper import get_random_text_and_number
from pages.compose_mail_page import *


def send_email(driver, mailer_page, current_page, subject, recipient='rocketbank-fan@yandex.ru',  text=get_random_text_and_number()):
    mailer_page.compose_email()
    current_page.send_email(recipient, subject, text)
    driver.get('https://mail.yandex.ru')
    wait_until(lambda: len(mail_indexes_of(subject, mailer_page.reload_and_fetch_mail())),6,1)
