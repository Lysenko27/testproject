import datetime
import time
import random
import string

def mail_indexes_of( mails,subject=None,author=None):
    if subject == None and author != None:
        return [i for i in range(len(mails)) if mails[i]['author'] == author]
    elif subject != None and author == None:
        return [i for i in range(len(mails)) if mails[i]['subject'] == subject]
    elif subject != None and author != None:
        return [i for i in range(len(mails)) if mails[i]['subject'] == subject and mails[i]['author'] == author]


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

