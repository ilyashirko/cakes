from django.core.mail import EmailMessage

from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, get_password


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            EmailMessage(
                subject='Регистрация на сайте CakeBake',
                body=(
                    f'Логин: {email}\nПароль: {get_password()}'
                ),
                to=[email]
            ).send()
            messages.success(request, f'Логин и пароль выслан на ваш email')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
        