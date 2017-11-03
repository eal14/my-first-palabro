from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Language

class LanguageForm(forms.ModelForm):
    
#    form_fields = ()

#    if(lng == 'es'):
#     form_fields = ('Descripcion','Descripcion_corta',)
#    else:
    form_fields = ('description','short_description',)

    class Meta:
        model = Language
        fields = ('description','short_description',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Your name please.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
