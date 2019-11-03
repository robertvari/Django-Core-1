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

    category_filter = request.GET.get("category")
    
    all_photos = Photo.objects.all()
    if category_filter:
        all_photos = [i for i in all_photos if i.category.name == category_filter]

    context = {
        "photos": all_photos
    }
    
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html')

def about(request):
    context = {
        "about": "This is a simple about text in a context."
    }
    
    return render(request, 'about.html', context)