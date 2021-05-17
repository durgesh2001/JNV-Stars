from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, "index.html")




def alumini(request):
    return render(request, "alumini.html")




def about(request):
    return render(request, "about.html")



def contact(request):
    return render(request, "contact.html")



def campus(request):
    return render(request, "campus.html")