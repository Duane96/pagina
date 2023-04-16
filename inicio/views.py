from django.shortcuts import render
from .models import Video
# Create your views here.

def inicioes(request):
    
    videos = Video.objects.all()
    return render(request, 'inicio/index.html', {'videos': videos})

def inicioen(request):
    
    videos = Video.objects.all()
    return render(request, 'inicio/indexen.html', {'videos': videos})