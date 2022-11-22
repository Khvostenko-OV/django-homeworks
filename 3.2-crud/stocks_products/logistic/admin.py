from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')

class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    inlines = (StockProductInline,)
    list_display = ('pk', 'address')

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'stock', 'product', 'quantity', 'price')
