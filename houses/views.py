from django.shortcuts import render
from .models import House

def index(request):
	xyz = House.objects.all()
	return render(request, 'houses/index.html', {'xyz': xyz})
