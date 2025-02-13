from django import forms
from .models import *

class InMailForm(forms.ModelForm):
    class Meta:
        model = InMail
        fields = ('own_company','init','side_two', 'in_number' , 'upload_file', 'response_to', 'topic', 'track_number')


class OutMailForm(forms.ModelForm):
    class Meta:
        model = OutMail
        fields = ('own_company','init','side_two', 'out_number' , 'upload_file', 'response_to', 'topic', 'track','track_number')


class EntityEdit(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ('adress',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)