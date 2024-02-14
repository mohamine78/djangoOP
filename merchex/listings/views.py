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
    return HttpResponse(f"""
                        <h1>Hello Django !</h1>
                        <p>Mes groupes préférés sont :</p>
                        <ul>
                        <li>{titles[0].title}</li>
                         <li>{titles[1].title}</li>
                          <li>{titles[2].title}</li>
                          <li>{titles[3].title}</li>
                        </ul>
                        """)
