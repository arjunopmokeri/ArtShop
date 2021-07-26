from django.contrib import admin
from .models.product import product
from .models.category import category
from .models.customer import customer
from .models.orders import Orders


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']


# Register your models here.
admin.site.register(product, AdminProduct)
admin.site.register(category, AdminCategory)
admin.site.register(customer, AdminCustomer)
admin.site.register(Orders)
