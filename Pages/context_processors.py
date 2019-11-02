from Photos.models import Category

def categories(request):
    context = {
        "categories": Category.objects.all().order_by("name")
    }

    return context