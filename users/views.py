from django.shortcuts import render


# Create your views here.
def index(request):
    """Homepage"""
    return render(request, 'users/index.html')
