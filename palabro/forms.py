from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

from .models import Language
from .models import Profile
from .models import Genre

class LanguageForm(forms.ModelForm):
    
#    form_fields = ()

#    if(lng == 'es'):
#     form_fields = ('Descripcion','Descripcion_corta',)
#    else:
    form_fields = (_('Description'),_('Short description'),)

    class Meta:
        model = Language
        fields = ('description','short_description',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text=_('Your name please.'))
    last_name = forms.CharField(max_length=30, required=False, help_text=_('Optional.'))
    email = forms.EmailField(max_length=254, help_text=_('Required. Inform a valid email address.'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserForm(forms.ModelForm):
    form_fields = (_('First name'),_('Last name'),_('Email'),)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        

class ProfileForm(forms.ModelForm):
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False)
    birthdate = forms.DateField(required=False)
    form_fields = (_('Native language'),_('Birthdate'),_('Genre'),)

    class Meta:
        model = Profile
        fields = ('native_language','birthdate','genre',)
        
