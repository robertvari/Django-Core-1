from django.shortcuts import render, HttpResponse

from Photos.models import Category

# Create your views here.
def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')

def about(request):
    context = {
        "about": "This is a simple about text in a context."
    }
    
    return render(request, 'about.html', context)