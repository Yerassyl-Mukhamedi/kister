from django import forms
from .models import *

class MailForm(forms.ModelForm):

    class Meta:
        model = InMail
        fields = ('own_company','side_two', 'in_number' , 'upload_file', 'response_to', 'topic')

