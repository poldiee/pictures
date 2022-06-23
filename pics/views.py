from django.shortcuts import render
# from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    # return render(request, 'pics/index.html')
    images = Image.objects.all()
    print (images)
    return render(request, 'pics/index.html', {'images': images[::-1]})
