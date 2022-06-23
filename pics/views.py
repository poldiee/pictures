from django.shortcuts import render
# from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    # return render(request, 'pics/index.html')
    images = Image.objects.all()
    print(images)
    return render(request, 'pics/index.html', {'images': images[::-1]})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        search_term = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(searched_images)
        return render(request, 'pics/search_results.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any image category"
        return render(request, 'pics/search_results.html', {"message": message})
