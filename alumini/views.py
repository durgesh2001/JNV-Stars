from django.shortcuts import render
from alumini.models import aluminies
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

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


def profile(request, pk):
    stu = aluminies.objects.get(id=pk)
    return render(request, "profile.html", {'stu': stu})


def search(request):
    query = request.GET['query']
    if len(query)>78:
        alumi = aluminies.objects.none()
    else :    
        alumiBatch = aluminies.objects.filter(batch__icontains = query)
        alumiName = aluminies.objects.filter(name__icontains = query)
        alumi = alumiBatch | alumiName

    params = {'alumi' : alumi, 'query' : query}
    return render(request, "search.html", params)


def ourteam(request):
    return render(request, "ourteam.html")
def gallery(request):
    return render(request, "gallery.html")