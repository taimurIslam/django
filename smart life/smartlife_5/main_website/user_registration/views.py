from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Registration


def view_registration_page(request):
    return render(request, 'registration.html')


def insert_register_form_values_in_database(request):
    if request.method == 'POST':
        user_registration_informations = Registration()
        user_registration_informations.first_name = request.POST['first_name']
        user_registration_informations.last_name = request.POST['last_name']
        user_registration_informations.phone_number = request.POST['phone_number']
        user_registration_informations.email_address = request.POST['email']
        user_registration_informations.user_name = request.POST['user_name']
        user_registration_informations.user_password = request.POST['password']
        user_registration_informations.user_address = request.POST['address']
        user_registration_informations.save()
        #print(user_registration_informations.name)
        return render(request, 'registration.html')

def registered_user_list(request):
    registered_user_list = Registration.objects.all()
    print(registered_user_list)
    return render(request, 'registered_user_list.html', {'registered_user_list': registered_user_list,} )


def registered_user_data_edit(request, registered_user_id ):
    #print(registered_user_id)
    #return HttpResponse("edited")
    registered_user_edit_or_delete_all_information = get_object_or_404(Registration, pk = registered_user_id)
    print(registered_user_edit_or_delete_all_information.phone_number)
    return render(request, 'registered_user_edit_or_delete.html',
                  {'registered_user_edit_or_delete_all_information': registered_user_edit_or_delete_all_information, })


def registered_user_data_delete(request, registered_user_id):
    registered_user_list = get_object_or_404(Registration, pk = registered_user_id)
    registered_user_list.delete()
    registered_user_list = Registration.objects.all()
    #return render(request, 'registered_user_list.html', {'registered_user_list': registered_user_list, })
    return redirect('registered_user_list')



def registered_user_data_edited(request, registered_user_id):
    if request.method == 'POST':
        user_registration_informations = get_object_or_404(Registration, pk = registered_user_id)
        user_registration_informations.first_name = request.POST['first_name']
        user_registration_informations.last_name = request.POST['last_name']
        user_registration_informations.phone_number = request.POST['phone_number']
        user_registration_informations.email_address = request.POST['email']
        user_registration_informations.user_name = request.POST['user_name']
        user_registration_informations.user_password = request.POST['password']
        user_registration_informations.user_address = request.POST['address']
        user_registration_informations.save()

        registered_user_list = Registration.objects.all()
        #return render(request, 'registered_user_list.html', {'registered_user_list': registered_user_list, })
        return redirect('registered_user_list')








