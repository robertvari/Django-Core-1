from django.urls import path

from .views import home, contact, about, category_view, photo_details

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),

    path('<int:photo_id>/', photo_details, name="photo_details"),
    path('<str:category>/', category_view, name="category_view"),
]