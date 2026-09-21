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
    list_display = ('product', 'user')



@admin.register(Product)
class ProductAdmin(unfold_admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title', 'description')
    # prepopulated_fields = {'slug': ('title',)}
    list_filter = ('brand', 'category')
    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.category.all()])
    get_categories.short_description = 'Категории'


@admin.register(ContactMessage)
class ContactMessageAdmin(unfold_admin.ModelAdmin):
    list_display = ('email', 'subject')


@admin.register(Category)
class CategoryAdmin(unfold_admin.ModelAdmin):
    list_display = ('name',)
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(unfold_admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Brand)
class BrandAdmin(unfold_admin.ModelAdmin):
    list_display = ('name',)







