from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Slider, Advertisement, SocialLink, Trailer, TrailerItem, Celebrity, News, Tweet, MovieTheater, MovieTV

def index(request):
    context = {
        'sliders': Slider.objects.all(),
        'social_links': SocialLink.objects.all(),
        'ads': Advertisement.objects.all(),
        'trailers': Trailer.objects.all(),
        'trailer_items': TrailerItem.objects.all(),
        'celebrities': Celebrity.objects.all(),
        'news': News.objects.all(),
        'tweets': Tweet.objects.all(),
        'movies_theater': MovieTheater.objects.all(),
        'movies_tv': MovieTV.objects.all(),
    }
    return render(request, 'index.html', context)

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        return HttpResponse('Subscribed successfully.')
    return render(request, 'base.html')