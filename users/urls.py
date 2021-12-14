from django.urls import path, include

app_name = 'users'  # This is the namespace

urlpatterns = [
    path('', include('django.contrib.auth.urls'))
]
