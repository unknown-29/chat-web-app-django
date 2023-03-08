from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.showHomePage,name="showHomePage"),
    path('createAccount',views.createAccount,name="createAccount"),
    path('forgotPassword',views.forgotPassword,name="forgotPassword"),
    path('changePassword',views.changePassword,name="changePassword"),
    path('validate',views.validate,name="validate"),
    path('dashboard',include("dashboard.urls")),
]
