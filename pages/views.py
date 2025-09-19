from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title': 'Home',
        'features': [
            'Django',
            'template',
            'static files',
        ]
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def gallery(request):
    images = [
        'img1.jpg',
        'img2.jpg',
        'img3.jpg',
    ]
    return render(request, 'home.html', {
        'title': 'Gallery',
        'images': images
    })

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)

def hello(request, name):
    return HttpResponse(f"Hello, {name}!")
