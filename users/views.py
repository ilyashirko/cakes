from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from string import ascii_letters, digits

from .forms import UserRegisterForm


def get_password():
        chars = ascii_letters + digits
        return get_random_string(12, chars)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/register.html', {'form': form})
        password = get_password()
        form.save(password)
        email = form.cleaned_data.get('email')
        EmailMessage(
            subject='Регистрация на сайте CakeBake',
            body=(
                f'Логин: {email}\nПароль: {password}'
            ),
            to=[email]
        ).send()
        messages.success(request, f'Логин и пароль выслан на ваш email')
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
