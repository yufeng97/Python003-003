from django.shortcuts import render
from django.http import HttpResponse
from .models import PhoneComment, ZdmPhone


# Create your views here.
def index(request):
    search = request.POST.get("search", "")
    articles = ZdmPhone.objects.all()
    for article in articles:
        if search:
            article.comments = PhoneComment.objects.filter(article_id=article.id, comment__contains=search)
        else:
            article.comments = PhoneComment.objects.filter(article_id=article.id)
    

    return render(request, 'index.html', locals())
