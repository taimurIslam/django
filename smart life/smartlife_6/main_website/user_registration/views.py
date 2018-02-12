from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .forms import *
from .models import Registration
from django.contrib import messages


def view_registration_page(request):
    form = Registration_Form()
    page_related_data = {
        'form':form,
        'title': 'Registration Page',
        'form_title': 'REGISTER FORM',
        'button_title': 'SUBMIT',
        'other_button_title': '',
    }
    return render(request, "registration.html", {'page_related_data':page_related_data, })


def insert_register_form_values_in_database(request):
    if request.method == 'POST':
        form_values = Registration_Form(request.POST)
        user_registration_informations = Registration()
        user_registration_informations.first_name = form_values['first_name'].value()
        user_registration_informations.last_name = form_values['last_name'].value()
        user_registration_informations.phone_number = form_values['phone_number'].value()
        user_registration_informations.email_address = form_values['email_address'].value()
        user_registration_informations.user_name = form_values['user_name'].value()
        user_registration_informations.user_password = form_values['user_password'].value()
        user_registration_informations.user_address = form_values['user_address'].value()
        user_registration_informations.save()

        return redirect('view_registration_page')


def registered_user_list(request):
    registered_user_list = Registration.objects.all()
    print(registered_user_list)
    return render(request, 'registered_user_list.html', {'registered_user_list': registered_user_list,} )


def registered_user_data_edit(request, registered_user_id ):
    registered_user_edit_or_delete_all_information = get_object_or_404(Registration, pk = registered_user_id)

    previous_data = {
        'first_name': registered_user_edit_or_delete_all_information.first_name,
        'last_name': registered_user_edit_or_delete_all_information.last_name,
        'phone_number':registered_user_edit_or_delete_all_information.phone_number,
        'email_address': registered_user_edit_or_delete_all_information.email_address,
        'user_name': registered_user_edit_or_delete_all_information.user_name,
        'user_password': registered_user_edit_or_delete_all_information.user_password,
        'user_address': registered_user_edit_or_delete_all_information.user_address,
    }
    #print(previous_data)
    form = Registration_Form(previous_data)
    page_related_data = {
        'form': form,
        'title': 'Update Registration Page',
        'form_title': 'UPDATE REGISTER FORM',
        'button_title': 'UPDATE',
        'other_button_title': 'CANCEL',
    }
    return render(request, 'registration.html', {'page_related_data': page_related_data,})


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

