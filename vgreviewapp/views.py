from django.shortcuts import render
from .models import Videogame

# Create your views here.
def index(request):
    return render(request, 'vgreviewapp/index.html')

def videogames(request):
    videogame_list=Videogame.objects.all()
    return render(request, 'vgreviewapp/videogames.html', {'videogame_list': videogame_list})