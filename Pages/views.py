from django.shortcuts import render, HttpResponse

from Photos.models import Photo

# Create your views here.
def home(request):
    context = {
        "photos": Photo.objects.all().order_by('uploaded').reverse()
    }

    return render(request, "home.html", context)

def category_view(request, category):
    context = {
        "photos": Photo.objects.filter(category__name=category).order_by('uploaded').reverse()
    }

    return render(request, "home.html", context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')