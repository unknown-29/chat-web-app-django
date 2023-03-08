from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.showDashboard,name="showDashboard"),
    path('/',views.showDashboard,name="showDashboard"),
    path('/chatSection',include('chatSection.urls')),
    # path('/send',include('chatSection.urls')),
]
