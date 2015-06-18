from django import forms
from django.forms.widgets import CheckboxInput
from .models import Join

class EmailForm(forms.Form):
    email = forms.EmailField()
    
    
class JoinForm(forms.ModelForm):
    class Meta:
        exclude = ['ip_address', 'ref_id']
        model = Join