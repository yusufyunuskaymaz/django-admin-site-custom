from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ("is_in_stock",)
    list_display_links = ("create_date","name")
    list_filter = ("is_in_stock", "create_date",)
    ordering = ("-update_date",)
    search_fields = ("name",)
    prepopulated_fields = {"slug" : ("name",)}
    list_per_page = 15
    date_hierarchy = "update_date"
    fields = (("name", "slug"), "description", "is_in_stock")



admin.site.register(Product, ProductAdmin)

admin.site.site_title = "Back End Site"
admin.site.site_header = "Deneme"
admin.site.index_title = "Deneme2"


# Register your models here.
