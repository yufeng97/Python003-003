from django.shortcuts import render
from django.http import HttpResponse
from .models import Ratings


def index(request):
    ratings = Ratings.objects.all()
    return render(request, 'index.html', locals())
