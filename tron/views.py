from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def onion(request):
    return HttpResponse("<h1><marquee>***********hello world****************</marquee></h1>")