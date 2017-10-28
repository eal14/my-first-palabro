from django.shortcuts import render

# Create your views here.
def palabro_list(request):
    return render(request, 'palabro/palabro_list.html', {})
