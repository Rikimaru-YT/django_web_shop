from django.contrib import admin
from unfold import admin as unfold_admin

from .models import (
    Category,
    Tag,
    Brand,
    ContactMessage,
    Product,
    ProductImage,
    ProductComment
)

class ProductImageInline(unfold_admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(ProductComment)
class ProductCommentAdmin(unfold_admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(unfold_admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]


@admin.register(ContactMessage)
class ContactMessageAdmin(unfold_admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(unfold_admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(unfold_admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(unfold_admin.ModelAdmin):
    pass



# admin.site.register([Category, Tag, Brand])
