from django.contrib import admin

# Register your models here.

from listings.models import Band


class BandAdmin(admin.ModelAdmin):
     # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('name', 'year_formed', 'genre')

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument


from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display =('title','year_created')
    
admin.site.register(Listing, ListingAdmin)