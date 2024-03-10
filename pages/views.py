from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home Page
def home(request):
    # grab some data from the database
    # some reinement of data here
    context = {
        "page_name": " our Website",
        "title": "Home"
    }
    return render(request, 'pages/home.html', context)

# About us
def about(request):
    context = {
        "page_name": "our About Page",
        "title" : "About"
    }
    return render(request, 'pages/about.html', context)

# Services
def services(request):
    context = {
        "page_name": " our Services Page",
        "title" : "Services"
    }
    return render(request, 'pages/services.html', context)

# Contact Us
def contact(request):
    context = {
        "page_name": "our Contact Page",
        "title" : "Contact"
    }
    return render(request, 'pages/contact.html', context)