from django.shortcuts import render
from alumini.models import aluminies
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

from .models import *

def index(request):
    return render(request, "index.html")




def alumini(request):
    alumni = aluminies.objects.all()   #.order_by('batch')
    paginator = Paginator(alumni, 10)  #we can set here "orphans" also 
    alumni_num = request.GET.get('page')
    alumni_obj = paginator.get_page(alumni_num)
    # return render(request, "alumini.html", {'alumi': alumi})
    return render(request, "alumini.html", {'alumni_obj': alumni_obj})




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