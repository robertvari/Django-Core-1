from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World!</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")