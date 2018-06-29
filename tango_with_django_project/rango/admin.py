from django.contrib import admin

from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('View information', {'fields': ['views', 'likes']}),
        ('Other information', {'fields': ['slug']}),
    ]
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
