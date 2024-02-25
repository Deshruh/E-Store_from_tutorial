from django.contrib import admin

from products.models import ProductCategory, Product

# admin.site.register(Product)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "category")
    # fields = ('image', 'name')
    # readonly_fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
