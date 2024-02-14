from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


# Create your views here.

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings\hello.html',
                  context={"bands":bands})

def about(request):
    return HttpResponse('<h1>About us</h1><p>Nous adorons Django</p>')

def contact(request):
    return HttpResponse('<h1>Contactez Nous!<h1><p>Pour plus de détails, veuillez nous contacter!</p>')

def list(request):
    titles = Listing.objects.all()
    return render(request, 'listings\listings.html',
                  context={"titles":titles})

