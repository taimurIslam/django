from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('(?P<locker_id>[0-9]+)/$', views.locker_data_response, name='locker_data_response'),
]