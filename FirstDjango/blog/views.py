from django.shortcuts import render
from django.http import HttpResponse



posts= [
    {
        "author": "Dio",
        "titolo": "Carogna",
        "content": "DODIODIODIDOIDOID"
    },
    {
        "author": "Madonna",
        "titolo": "Cagna",
        "content": "MARIAAAAAAAAAAAA"
    },

]
# Create your views here.
def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title": "About"})



