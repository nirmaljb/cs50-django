from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    current = datetime.now()
    month = current.month
    day = current.day
    
    status = month == 1 and day == 1

    return render(request, "newyear/index.html", {
        "newyear": status
    })