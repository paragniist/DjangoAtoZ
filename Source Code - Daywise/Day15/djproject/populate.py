import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djproject.settings')

import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *

fake=Faker()

def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)


def populate(n):
    for i in range(n):    
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Manage','TL','IT Engineer'))
        felegibility=fake.random_element(elements=('B.tech','M.tech','MCA','PHD'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hydjob_record=Hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=felegibility,address=faddress,email=femail,phonenumber=fphonenumber)
        #hydjob_record=Hydjobs.objects.get_or_create(company=fcompany)
        print(fdate)


populate(25)    
    
