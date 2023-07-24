from django.urls import path,re_path
from app.views import *

app_name = 'app'
urlpatterns = [
    path('',show,name='show_page'),
    re_path(r'^complete/(?P<pk>\d+)/$', complete, name='complete-button'),
    re_path(r'^edit/(?P<pk>\d+)/$', edit, name='edit-button'),
    re_path(r'^delete/(?P<pk>\d+)/$',delete,name='delete-button'),
    path('add/',add,name='add_page')
]