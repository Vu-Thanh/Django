from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>contact_view!</h1>")
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [1, 2, 3, 4, 5],
        "title": "lalala",
    }

    # return HttpResponse("<h1>about_view!</h1>")
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    # return HttpResponse("<h1>social_view!</h1>")
    return render(request, "social.html", {})
