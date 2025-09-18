from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home',
        'features' : [
            'Django',
            'template',
            'static files',
            
            ]

    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})