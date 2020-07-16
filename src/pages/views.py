from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    my_context = {
        "myname": "Astor",
        "myage": 27,
        "myskills": ['js', 'css', 'html', 'django', 2],
        "programer": 'senior'
    }
    return render(request, "home.html", my_context)


def contact_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World from contact</h1>')
