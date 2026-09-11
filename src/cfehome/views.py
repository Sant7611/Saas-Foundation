from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits




def home_view(request):
    page_title = "Home Page"
    path = request.path
    PageVisits.objects.create(path=path)
    querysets = PageVisits.objects.filter(path=path)
    context ={
        'page_title': page_title,
        'querysets':querysets.count()
    }
    
    return render(request, 'home.html', context)