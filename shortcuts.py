from selenium import webdriver
from pages.login_page import *
from pages.mailer_main_page import *
from pages.compose_mail_page import *
import time

def send_email(driver, recipient, subject, text):
    MailerMainPage(driver).compose_email()
    time.sleep(5)
    current_page = ComposeMailPage(driver)
    current_page.send_email(recipient, subject, text)
    driver.get('https://mail.yandex.ru')
