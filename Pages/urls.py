from django.urls import path

from .views import ContactView, HomeView, AboutView, CategoryView, PhotoDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('<str:category>/', CategoryView.as_view(), name="categories"),
    path('stilus/contact/', ContactView.as_view(), name="contact"),
    path('stilus/about/', AboutView.as_view(), name="about"),
    path('<str:category>/<int:pk>/', PhotoDetailsView.as_view(), name="photo_details"),
]