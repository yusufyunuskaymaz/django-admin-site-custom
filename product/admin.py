from django.contrib import admin
from .models import Product

admin.site.register(Product)

admin.site.site_title = "Back End Site"
admin.site.site_header = "Deneme"
admin.site.index_title = "Deneme2"


# Register your models here.
