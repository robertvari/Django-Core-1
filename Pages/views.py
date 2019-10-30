from django.shortcuts import render, HttpResponse, redirect

from Photos.models import Photo

from django.core.mail import send_mail
from .forms import ContactForm

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

def photo_view(request, category, photo_title):
    context = {
        "photo": Photo.objects.get(title=photo_title)
    }

    return render(request, "photo_details.html", context)

def about(request):
    return render(request, 'about.html')

def successView(request):
    return render(request, "success.html")

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            
            send_mail(
                subject, # subject
                message, # message
                email, # from mail
                ['admin@example.com'] # to mails
            )

            return redirect("success")

    return render(request, 'contact.html', {"form":form})