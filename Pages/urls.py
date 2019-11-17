from django.urls import path

from .views import ContactView, photo_details, HomeView, AboutView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<str:category>/', CategoryView.as_view(), name="categories"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('about/', AboutView.as_view(), name="about"),
    path('<int:photo_id>/', photo_details, name="photo_details"),
]