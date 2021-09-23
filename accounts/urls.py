# accounts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('search',views.search, name='search'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('profile',views.profile,name='profile'),
    
]