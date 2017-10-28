from django.shortcuts import render

from .models import Language

# Create your views here.
def palabro_list(request):
    languages = Language.objects.all()
    return render(request, 'palabro/language_list.html', {'languages': languages})
