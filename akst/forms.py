from django import forms
from .models import suggestion

class SuggestionForm(forms.ModelForm):
    class Meta:
        model=suggestion
        fields=('email','message')