from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views


urlpatterns = [
    url(r'users/', views.index, name='users'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
