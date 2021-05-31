from django.shortcuts import render
from alumini.models import aluminies

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


<<<<<<< HEAD
# def student(request, pk):
#     stu = aluminies.objects.get(id=pk)
#     return render(request, "student.html", {'stu': stu})

def profile(request, pk):
    stu = aluminies.objects.get(id=pk)
    return render(request, "profile.html", {'stu': stu})
=======
def profile(request, pk):
    stu = aluminies.objects.get(id=pk)
    return render(request, "profile.html", {'stu': stu})


def search(request):
    query = request.GET['query']
    if len(query)>78:
        alumi = []
    else :    
        alumiBatch = aluminies.objects.filter(batch__icontains = query)
        alumiName = aluminies.objects.filter(name__icontains = query)
        alumi = alumiBatch | alumiName

    params = {'alumi' : alumi, 'query' : query}
    return render(request, "search.html", params)
>>>>>>> ad17418e78d86855387a579f73d027a934cc21e7
