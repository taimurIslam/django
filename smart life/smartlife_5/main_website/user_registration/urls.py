from django.urls import path, re_path
from . import views

urlpatterns = [

    re_path('^$', views.view_registration_page, name='view_registration_page'),
    re_path('^new_user_registered/$', views.insert_register_form_values_in_database, name='insert_register_form_values_in_database'),
]