import random
from datetime import datetime,timedelta

def custom_syntax(text):
    text = name(text)
    text = date(text)
    return text



### definition

from dictionnary import last_name, first_name

def name(text):
    text = text.replace('~ln',last_name[random.randint(0, len(last_name))].lower())
    text = text.replace('~fn',first_name[random.randint(0, len(first_name))].lower())
    return text


def date(text):
    epoch = datetime(1970, 1, 1)
    random_date = epoch + timedelta(seconds=random.randint(0, int((datetime.now() - epoch).total_seconds())))

    text = text.replace('~ddb',random_date.strftime("%Y-%m-%d %H:%M:%S"))
    text = text.replace('~da',random_date.strftime("%m/%d/%Y"))
    text = text.replace('~de',random_date.strftime("%d/%m/%Y"))
    return text