from django.contrib import admin
from product.models import ProductImage, Product


class ProductImageInlineAdmin(admin.StackedInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInlineAdmin]
    list_display = ['title', 'posted_by', 'category', 'price', 'discount_price', 'is_feature', 'status']
    list_filter = ['category__name', 'is_feature', 'status', 'created_at']
    search_fields = ['title', 'category__name']
