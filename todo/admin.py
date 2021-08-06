from django.contrib import admin
from .models import Item  #.models means models file in the current directory

# Register your models here.
admin.site.register(Item)
