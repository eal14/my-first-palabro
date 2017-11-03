from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from .models import Language
from .models import Visitor
from .models import Visit

from .forms import LanguageForm
from .forms import SignUpForm

from django.contrib.gis.geoip import GeoIP

# Create your views here.
def language_list(request):
    languages = Language.objects.all()
    lng = 'es'
    html_location = lng + '/palabro/language_list.html'
    return render(request, html_location, {'languages': languages})

def init(request):
    ip = get_ip_address(request)
    lng = save_visitor_info(ip, 'init')
    html_location = lng + '/palabro/init.html'
    return render(request, html_location,{})

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


def save_visitor_info(ip, visited_page):
    lng = 'es'
    
    g = GeoIP()
    visitor_info = g.city(ip)
    if visitor_info:
        visitor = Visitor.objects.get(pk=ip)
        if visitor:
            visitor.counter += 1
            visitor.save()

            visit = Visit.objects.create(visited_page=visited_page)
            visit.visitor = visitor
            visit.save()            
            
        else:
            visitor = Visitor.objects.create(ip=ip, city=visitor_info['city'], country_code=visitor_info['country_code'], country_code3=visitor_info['country_code3'], latitude=visitor_info['latitude'], longitude=visitor_info['longitude'], counter=1)
            visitor.save()            
            
            visit = Visit.objects.create(visited_page=visited_page)
            visit.visitor = visitor
            visit.save()
            
            if visitor.country_code3 == 'MEX':
                lng = 'es'
    return lng
