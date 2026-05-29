from django.urls import path
from .views import (login_page,request_page,dashboard_page,detail_page,)

urlpatterns = [
    path('',login_page,name='login'),
    path('request/',request_page,name='request'),
    path('dashboard/',dashboard_page,name='dashboard'),
    path('request/<int:id>/',detail_page,name='detail'),
]