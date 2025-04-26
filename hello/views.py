from datetime import datetime
import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_there(request, name='RVI'):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# Replace the existing home function with the one below
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

