from django.contrib import admin

from category.models import Category
from product.models import Product


class ProductInlineAdmin(admin.StackedInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInlineAdmin]
    list_display = ['name', 'status']
