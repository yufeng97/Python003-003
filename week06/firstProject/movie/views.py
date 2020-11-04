from django.shortcuts import render
from django.http import HttpResponse
from .models import Ratings


def index(request):
    conditions = {'star__gt': 3}

    search = request.POST.get('search', '')

    if search:
        conditions['comment__contains'] = search
    ratings = Ratings.objects.filter(**conditions)
    
    return render(request, 'index.html', locals())
