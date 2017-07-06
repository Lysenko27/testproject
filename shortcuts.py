from helper import get_random_text_and_number,wait_until, mail_indexes_of


def send_email(driver, mailer_page, current_page, subject, recipient='rocketbank-fan@yandex.ru',  text=get_random_text_and_number()):
    current_page.send_email(recipient, subject, text,mailer_page)
    driver.get('https://mail.yandex.ru')
    wait_until(lambda: len(mail_indexes_of(mails=mailer_page.reload_and_fetch_mail(), subject=subject)),6,1)
