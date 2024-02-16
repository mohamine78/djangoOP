from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail 
from django.shortcuts import redirect 



# Create your views here.

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def article(request):
    titles = Listing.objects.all()
    return render(request, 'listings\listings.html',
                  context={"titles":titles})

def about(request):
    return HttpResponse('<h1>About us</h1><p>Nous adorons Django</p>')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
    
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
            return redirect("email-envoyer")
    else:
        form = ContactUsForm()

    return render(request,
        'listings/contact.html',
        {'form': form})     
        

    
  