from django.contrib import admin
from .models import Client,Validity,ClientValidity,Place,PlaceCategoryPlace,CategoryPlace,Coach,PlaceCoach

# Register your models here.
admin.site.register(Client)
admin.site.register(Validity)
admin.site.register(ClientValidity)
admin.site.register(Place)
admin.site.register(PlaceCategoryPlace)
admin.site.register(CategoryPlace)
admin.site.register(Coach)
admin.site.register(PlaceCoach)

