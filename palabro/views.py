from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from .models import Language

from .forms import LanguageForm
from .forms import SignUpForm

#from .general_lib import GenLib

# Create your views here.
def language_list(request):
    languages = Language.objects.all()
    lng = 'es'
    html_location = lng + '/palabro/language_list.html'
    return render(request, html_location, {'languages': languages})

def init(request):
    ip = get_ip_address(request)
    lng = 'es'
    html_location = lng + '/palabro/init.html'
    return render(request, html_location,{ 'ip': ip})

def dashboard(request):
    lng = 'es'
    html_location = lng + '/palabro/dashboard.html'
    return render(request, html_location,{})

def register(request):
    lng = 'es'
    html_location = lng + '/palabro/register.html'
    return render(request, html_location,{})

@login_required
def language_new(request):
    lng = 'es'
    if request.method == "POST":
        form = LanguageForm(request.POST)

        if form.is_valid():
            language = form.save(commit=False)
            language.save()
            return redirect('language_list')
    else:
        form = LanguageForm()
    html_location = lng + '/palabro/language_edit.html'
    return render(request,html_location, {'form': form})

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
    lng = 'es'
    html_location = lng + '/registration/signup.html'
    return render(request, html_location, {'form': form})

def get_ip_address(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    if ip:
        ip = ip.split(", ")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip
