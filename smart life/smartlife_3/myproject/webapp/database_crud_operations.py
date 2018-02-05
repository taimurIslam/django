from .models import *
from django.http import HttpResponse


def login_table_insertion():
    pass

def login_table_edit():
    pass
def login_table_delete():
    pass

def registration_table_insertion(request):
    if request.method == 'POST':

        print ("hello")
        user_Name = request.POST.get('user_Name','')
        user_Email = request.POST.get('user_Email', '')
        user_Phone_Number = request.POST.get('user_Phone_Number', '')
        user_Address = request.POST.get('user_Address', '')
        user_password = request.POST.get('user_password', '')

        insert = registration(user_Name=user_Name, user_Email=user_Email, user_Phone_Number=user_Phone_Number, user_Address=user_Address, user_password=user_password)
        insert.save()
        return HttpResponse("done")
def registration_table_edit():
    pass
def registration_table_delete():
    pass

def device_table_insertion():
    pass
def device_table_edit():
    pass
def device_table_delete():
    pass
