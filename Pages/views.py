from django.shortcuts import render, HttpResponse

from Photos.models import Photo

# Create your views here.
def get_random_photos():
    '''
    Get random photos for testing CSS grid
    '''
    
    photo_list = []
    for index in range(20):
        photo_list.append(
            {
                "name": f"Photo {index}", 
                "url":f"https://source.unsplash.com/1100x600/?nature{index}",
                "description": f"Photo {index} description..."
            }
        )
    
    return photo_list

def home(request):
    context = {
        "photos": Photo.objects.all()
    }
    
    return render(request, 'home.html', context)


def category_view(request, category):
    context = {
        "photos": Photo.objects.filter(category__name=category),
        "category":category,
    }

    return render(request, 'categories.html', context)


def photo_details(request, photo_id):
    context = {
        "photo": Photo.objects.get(pk=photo_id)
    }

    return render(request, 'photo_details.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    context = {
        "about": "This is a simple about text in a context."
    }
    
    return render(request, 'about.html', context)