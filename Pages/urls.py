from django.urls import path

from .views import home, contact, about, category_view

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('<str:category>/', category_view, name="category_view"),    
]