from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string



def get_password():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(12, chars)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'email',
        ]

    def clean(self):
        super().clean()
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('E-mail адрес уже используется.')
        return self.cleaned_data
    
    def save(self):
        user = super(UserRegisterForm, self).save(commit=False)
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            user.username = email
            user.set_password(get_password())
            user.save()
