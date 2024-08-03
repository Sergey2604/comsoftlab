from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('get_emails/', views.get_emails, name='get_emails'),
]
