from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from .models import Language

from .forms import LanguageForm
from .forms import SignUpForm

# Create your views here.
def language_list(request):
    languages = Language.objects.all()
    return render(request, 'palabro/language_list.html', {'languages': languages})

def init(request):
    return render(request, 'palabro/init.html',{})

def dashboard(request):
    return render(request, 'palabro/dashboard.html',{})

def register(request):
    return render(request, 'palabro/register.html',{})

@login_required
def language_new(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)

        if form.is_valid():
            language = form.save(commit=False)
            language.save()
            return redirect('language_list')
    else:
        form = LanguageForm()
    return render(request,'palabro/language_edit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
