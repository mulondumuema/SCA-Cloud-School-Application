from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to SCA Cloud School Application , this is my first assessment")