
from django.contrib import admin
# import your models here
from .models import Cards, Selling

# Register your models here
admin.site.register(Cards)
admin.site.register(Selling)