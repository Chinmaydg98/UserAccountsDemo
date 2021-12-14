from django.urls import path, include
from . import views

app_name = 'users'  # This is the namespace

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
