from django.shortcuts import render, HttpResponse

from Photos.models import Photo

# Create your views here.
def home(request):
    context = {
        "photos": Photo.objects.all()
    }
    
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html')

def about(request):
    context = {
        "about": "This is a simple about text in a context."
    }
    
    return render(request, 'about.html', context)