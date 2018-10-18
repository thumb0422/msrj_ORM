# -*- coding: utf-8 -*-
from datetime import datetime
import random
import string

def generate_random_str(randomlength=16):
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str

def generate_orderId(preStr='YY'):
    result = preStr + datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3] + generate_random_str(4)
    return result