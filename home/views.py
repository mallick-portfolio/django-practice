from django.shortcuts import render
from django.shortcuts import render
# Create your views here.


def home(request):
    data = {
        "title": "Home page",
        "name": "Tamal",
        "subjects": ["bangla", "english", "physics", "chemistry"]
    }
    return render(request, "index.html", data)
