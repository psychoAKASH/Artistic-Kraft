from django.shortcuts import render
from .generate import gene


def home_view(request):
   
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, 'pages/contact.html')


def genimg(request):
    img1 = {}
    img2 = {}
    img3 = {}
    if request.method == "POST":
        text = request.POST.get('prompt')
        result = gene(text)
        img1 = result[0]
        img2 = result[1]
        img3 = result[2]

    return render(request, 'pages/home.html', {'response1': img1, 'response2': img2, 'response3': img3})