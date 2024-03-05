from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        input_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'] 
