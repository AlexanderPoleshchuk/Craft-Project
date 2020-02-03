from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.views.decorators.http import require_GET

# Create your views here.
def registration(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'registration.html', context={
            "form": form})
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            link = user.get_verification_link()
            user.email_user(
                "Email confirmation",
                f"Please follow the <a href='{link}'>link</a>",
                from_email='admin@bio.com'
            )
            user.verification_email_sent_at = timezone.now()
            user.save()
            return redirect("/")
        else:
            return render(request, 'registration.html', context={
                "form": form
            })


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', context={
            "error": False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/verify-email')

        else:
            return render(request, 'login.html', context={
                "error": True
            })


@login_required
@require_GET
def verify_view(request):
    print(request.GET.get('key'))
    secret_ket = request.GET.get('key')
    print(secret_ket)
    if request.user.check_key(secret_ket):
        return render(request, 'confirmation_success.html')
    else:
        return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/")