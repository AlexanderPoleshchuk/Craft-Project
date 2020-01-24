from django.shortcuts import render
from users.forms import RegistrationForm


# Create your views here.
def registration(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'registration.html', context={
            "form": form})


def login(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'login.html', context={
            "form": form})
