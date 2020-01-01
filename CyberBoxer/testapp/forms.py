from django import forms
class Registration(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    name=forms.CharField()
    phone=forms.IntegerField()
