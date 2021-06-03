from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def auto(request, magnet_link):
    return HttpResponse(f"This is your link: {magnet_link}")