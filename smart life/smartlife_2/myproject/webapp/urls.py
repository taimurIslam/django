from . import views
from django.urls import path

urlpatterns = [
    path('', views.DeviceList.as_view(), name='DeviceList'),
    # path('', views.DeviceMatch, name='DeviceMatch'),
    path('<int:id>/', views.DeviceMatch, name='DeviceMatch'),
]