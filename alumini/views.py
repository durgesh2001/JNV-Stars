from django.shortcuts import render

# Create your views here.

from .models import *

def index(request):
    return render(request, "index.html")




def alumini(request):
    alumi = aluminies.objects.all()
    return render(request, "alumini.html", {'alumi': alumi})




def about(request):
    return render(request, "about.html")



def contact(request):
    return render(request, "contact.html")



def campus(request):
    return render(request, "campus.html")


def student(request, pk):
    stu = aluminies.objects.get(id=pk)
    return render(request, "student.html", {'stu': stu})