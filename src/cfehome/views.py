from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits




def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)


def about_view(request, *args, **kwargs):
    qs=PageVisits.objects.all()
    path = request.path
    querysets = PageVisits.objects.filter(path=path)
    try:
        percent = (querysets.count() * 100.0)/qs.count()
    except:
        percent = 0
    
    context ={
        'page_title': "Home Page",
        'querysets':querysets.count(),
        'percent':percent
    }
    PageVisits.objects.create(path=path)
    
    return render(request, 'home.html', context)
