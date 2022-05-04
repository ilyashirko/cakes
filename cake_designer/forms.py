from django import forms

class GetPhone(forms.Form):
    phone = forms.CharField()