from django.contrib import admin
from bookmarks.models import Category, Link

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name", )}

class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'category','rating','description')
    search_fields = ('description',)
    list_filter = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)