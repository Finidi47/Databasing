from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render

from sacco.models import Customer


# Create your views here.
def test(request):
    # save a customer
    c1 = Customer(first_name ='saida',last_name= 'ali',
                  email='saida@gmail.com', dob='2010-11-28',
                  gender='Female', weight='62')
    c1.save()

    c2 = Customer(first_name='Jake', last_name='Juma',
                  email='juma23@gmail.com', dob='2001-11-28',
                  gender='Male', weight='55')
    c2.save()


    return HttpResponse("Ok, Done")