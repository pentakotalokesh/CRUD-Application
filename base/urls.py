from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginPage,name="login"),
    path('home/',views.home,name='home'),
    path('logout/',views.logoutPage,name='logout'),
    path('register_form/',views.CreateUser,name='CreateUser'),
    path('delete-Person/<str:pk>/',views.DeletePerson,name="DeletePerson"),
    path('update-person/<str:pk>/',views.UpdatePerson,name="UpdatePerson"),
    path('Create/',views.register,name='register')
    
]