from django.urls import path

from .views import home, contact, about, category_view, photo_view, successView

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('success/', successView, name="success"), 
    path('<str:category>/', category_view, name="category_view"),    
    path('<str:category>/<str:photo_title>', photo_view, name="photo_view"),    
]