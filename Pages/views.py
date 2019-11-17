from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, FormView, ListView, DetailView

from Photos.models import Photo
from .models import About
from .forms import ContactForm
import random


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["background_photo"] = random.choice( Photo.objects.all() )

        return context


class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photo_details.html'
    context_object_name = "photo"


class CategoryView(ListView):
    template_name = "categories.html"
    model = Photo
    context_object_name = "photos"

    def get_queryset(self):
        category_name = self.kwargs["category"]
        return self.model.objects.filter(category__name=category_name)

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        print(
            form.data["name"],
            form.data["email"],
            form.data["message"],
        )

        return super().form_valid(form)

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["about"] = About.objects.all()
        
        return context