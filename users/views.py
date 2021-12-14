from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def index(request):
    """Homepage"""
    return render(request, 'users/index.html')


def register(request):
    """User registration"""
    if request.method != 'POST':
        # First request means just display registration form
        form = UserCreationForm()
    else:
        # Means registration data received, now: Validate, Register User & Login
        form = UserCreationForm(data=request.POST)

        # Validate
        if form.is_valid():
            # Register User
            new_user = form.save()

            # Login
            login(request, new_user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
