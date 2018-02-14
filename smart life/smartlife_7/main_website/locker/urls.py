from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.locker_data_response, name = 'locker_data_response'),
]