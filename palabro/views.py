from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.sessions import *

from django.contrib.gis.geoip import GeoIP

from django.shortcuts import render
from django.shortcuts import redirect

from django.utils import translation

from django.views.generic import TemplateView

from django.db import IntegrityError, transaction

from .models import Language
from .models import Visitor
from .models import Visit
from .models import Profile

from .forms import LanguageForm
from .forms import SignUpForm
from .forms import UserForm
from .forms import ProfileForm

# Create your views here.

@login_required
def language_list(request):
    
    def_language(request)
    ip = get_ip_address(request)
    save_visitor_info(ip, 'language_list')
    
    languages = Language.objects.all()
    html_location = 'palabro/language_list.html'
    
    return render(request, html_location, {'languages': languages})


def index(request):
    
    def_language(request)
    ip = get_ip_address(request)
    save_visitor_info(ip, 'index')
    
    html_location = 'palabro/index.html'
    
    return render(request, html_location,{})

@login_required
def dashboard(request):
    
    def_language(request)
    ip = get_ip_address(request)
    save_visitor_info(ip, 'dashboard')
    
    html_location = 'palabro/dashboard.html'
    
    return render(request, html_location,{})


def register(request):
    
    ip = get_ip_address(request)
    save_visitor_info(ip, 'register')
    
    html_location = 'palabro/register.html'
    
    return render(request, html_location,{})

@login_required
def language_new(request):
    
    def_language(request)
    ip = get_ip_address(request)
    save_visitor_info(ip, 'language_new')
    
    if request.method == "POST":
        form = LanguageForm(request.POST)

        if form.is_valid():
            
            language = form.save(commit=False)
            language.save()
            
            return redirect('language_list')
    else:
        form = LanguageForm()
    
    html_location = 'palabro/language_edit.html'
    
    return render(request,html_location, {'form': form})


def signup(request):
    
    ip = get_ip_address(request)
    save_visitor_info(ip, 'signup')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            return redirect('profile')
    else:
    
        if request.user.is_authenticated():
            return redirect('dashboard')
            
        form = SignUpForm()
        
    html_location = 'registration/signup.html'
    
    return render(request, html_location, {'form': form})
    
@login_required
def configuration(request):
    
    ip = get_ip_address(request)
    save_visitor_info(ip, 'configuration')
    
    msg = ''
    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        
        if form.is_valid():
        
            profile = form.save(commit=False)
            profile.save()
            
            msg = 'Changes applied correctly.'
    else:
    
        try:
            profile = Profile.objects.get(pk=request.user.username)
            form = ProfileForm(profile)
            
        except Profile.DoesNotExist:
            form = ProfileForm()
    
    return render(request, 'palabro/configuration.html', {'form': form, 'msg': msg})
    
    
@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
#            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('dashboard')
#        else:
#            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'palabro/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




def get_ip_address(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    if ip:
        ip = ip.split(", ")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip


def save_visitor_info(ip, visited_page):    

    g = GeoIP()
    visitor_info = g.city(ip)
    
    if visitor_info:
        
        try:
            visitor = Visitor.objects.get(pk=ip)
            visitor.counter += 1
            visitor.save()

            visit = Visit.objects.create(visitor = visitor, visited_page=visited_page)
            visit.save()            
            
        except Visitor.DoesNotExist:
            visitor = Visitor.objects.create(ip=ip, city=visitor_info['city'], country_code=visitor_info['country_code'], country_code3=visitor_info['country_code3'], latitude=visitor_info['latitude'], longitude=visitor_info['longitude'], counter=1)
            visitor.save()            
            
            visit = Visit.objects.create(visitor = visitor, visited_page=visited_page)
            visit.save()
            

def def_language(request):

    if request.user.is_authenticated():
    
        if "LANGUAGE_SESSION_KEY" in request.session:
            translation.activate(request.session["LANGUAGE_SESSION_KEY"])
        else:
            request.session["LANGUAGE_SESSION_KEY"] = "es"
            translation.activate("es")

