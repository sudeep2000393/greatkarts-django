from django.contrib import admin
from .models import Product, Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock',
                    'is_available', 'modified_date', 'category')
    prepopulated_fields = {'slug': ('product_name',)}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product',
                    'is_active', 'variation_value', 'variation_category')
    list_editable = ('is_active',)
    list_filter = ('product',
                   'variation_value', 'variation_category')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
