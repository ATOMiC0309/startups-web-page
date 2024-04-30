from django.shortcuts import render
from .models import StartUpType, StartUp, Category


# Create your views here.

def index(request):
    startuptypes = StartUpType.objects.all()
    categories = Category.objects.all()
    startups = StartUp.objects.all()

    context = {
        'startuptypes': startuptypes,
        'startups': startups,
        'categories': categories,
    }
    return render(request, 'app/index.html', context=context)


def startup_detail(request, pk):
    startup = StartUp.objects.get(pk=pk)
    return render(request, 'app/detail.html', context={'startup': startup})


def category_by_types(request, pk):
    startupstype = StartUpType.objects.get(pk=pk)
    startupstypes = StartUpType.objects.all()
    categories = Category.objects.filter(types=startupstype)
    context = {
        'startuptypes': startupstypes,
        'categories': categories,
    }
    return render(request, 'app/index.html', context=context)


def startups_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    startups = StartUp.objects.filter(category=category)
    startupstypes = StartUpType.objects.all()
    categories = Category.objects.all()
    context = {
        'startuptypes': startupstypes,
        'startups': startups,
        'categories': categories,

    }
    return render(request, 'app/index.html', context=context)

def page_not_fount(request):
    return render(request, 'app/page404.html')

