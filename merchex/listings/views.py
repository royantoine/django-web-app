# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(
        request, 
        'listings/hello.html',
        {'bands': bands}
    )

def about(request):
    return render(
        request, 
        'listings/about.html',
    )

def listings(request):
    listings_ = Listing.objects.all()
    return render(
        request, 
        'listings/listings.html',
        {'listings_': listings_}
    )

def contact_us(request):
    return render(
        request, 
        'listings/contact.html',
    )
