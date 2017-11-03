from django.http import HttpRequest

class GenLib():
    
    #https://djangosnippets.org/snippets/2575/
    def get_ip_address(request):
        ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
        if ip:
            ip = ip.split(", ")[0]
        else:
            ip = request.META.get("REMOTE_ADDR", "")
        return ip
