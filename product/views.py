from urllib import request
from django.shortcuts import render
from datetime import datetime
from product.models import Contact  # Make sure this is correct
from django.contrib import messages

def index(request):
    messages.success(request, "Welcome to the index page!")
    return render(request, "index.html. ")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        discription = request.POST.get("discription")

        new_contact = Contact(
            name=name,
            email=email,
            phone=phone,
            discription=discription,
            datetime=datetime.today()
        )
        new_contact.save()
        messages.success(request, "massage was secess.")
    
    return render(request, "contact.html")


