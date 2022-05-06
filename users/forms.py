from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
    
    def save(self, password):
        user = super(UserRegisterForm, self).save(commit=False)
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            user.username = email
            user.set_password(password)
            user.save()
