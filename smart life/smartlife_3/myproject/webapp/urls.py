from . import views, database_crud_operations
from django.urls import path


app_name = 'webapp'

urlpatterns = [
    path('' , views.DeviceList.as_view(), name = 'DeviceList'),
    path('<int:id>/', views.DeviceMatch,  name = 'DeviceMatch'),
    path('login/', views.login,  name = 'login'),

    path('registration/', views.registration,  name = 'registration'),
    path('registration_table_insertion', database_crud_operations.registration_table_insertion,  name = 'registration_table_insertion'),
        ]