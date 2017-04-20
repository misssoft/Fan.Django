from django.shortcuts import render
from django.http import HttpResponse
from .models import School

# Create your views here.
def home(request):
    all = School.objects.all()
    primary = all.filter(phase = "P")
    secondary = all.filter(phase = "S")
    alevel = all.filter(phase = "A")
    context = {
        'primary': primary,
        'secondary':secondary,
        'alevel':alevel
    }
    return render(request,"main/home.html", context)
