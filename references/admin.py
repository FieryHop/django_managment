from django.contrib import admin
from .models import Status, Type, Category, SubCategory


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_type')
    list_filter = ('category__type', 'category')
    search_fields = ('name',)

    def get_type(self, obj):
        return obj.category.type.name

    get_type.short_description = 'Тип операции'

# Register your models here.
