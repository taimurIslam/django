from django.urls import path, re_path
from . import views

#app_name = 'music'
urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('(?P<album_id>[0-9]+)/$', views.view_details, name='view_details'),
    re_path('(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),


]