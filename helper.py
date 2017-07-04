import datetime
import time
import random
import string

def mail_indexes_of(subject, mail):
    mail_indexes = []
    for i in (range(0,len(mail))):
        if mail[i]['subject'] == subject:
          mail_indexes.append(i)
    return(mail_indexes)


def get_random_text_and_number(n=15, m=30):
    # генерация  символов(больших и малый)
    return ''.join([random.choice(string.ascii_letters) for i in range(random.randint(n, m))])


def wait_until(func, timeout, required_quantity_email):
    new_date = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
    event =False
    while datetime.datetime.now() < new_date:
        if func() == required_quantity_email:
            event=True
            break
        time.sleep(0.25)
    if event == False: raise(BaseException('Событиене не наступило'))

