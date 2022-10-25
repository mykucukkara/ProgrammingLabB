from django.contrib import admin

from product.models import Category, Product


# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    list_filter = ['status']

class productAdmin(admin.ModelAdmin):
    list_display = ['title','category']
    list_filter = ['status']

admin.site.register(Category, categoryAdmin)
admin.site.register(Product,productAdmin)