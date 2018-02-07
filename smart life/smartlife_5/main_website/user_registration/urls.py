from django.urls import path, re_path
from . import views

urlpatterns = [

    re_path('^$', views.view_registration_page, name='view_registration_page'),
    re_path('^new_user_registered/$', views.insert_register_form_values_in_database,
            name='insert_register_form_values_in_database'),
    re_path('^registered_user_list/$', views.registered_user_list, name='registered_user_list'),
    re_path('^registered_user_data_edit/(?P<registered_user_id>[0-9]+)/$',
            views.registered_user_data_edit, name='registered_user_data_edit'),
    re_path('^registered_user_data_delete/(?P<registered_user_id>[0-9]+)/$',
            views.registered_user_data_delete, name='registered_user_data_delete'),

    re_path('^registered_user_data_edited/(?P<registered_user_id>[0-9]+)/$',
            views.registered_user_data_edited, name='registered_user_data_edited'),

]