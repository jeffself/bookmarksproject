from django.contrib import admin
from bookmarks.models import Category, Link

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {"slug": ("name", )}

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title','url','submitted_by','category','rating','description')
    prepopulated_fields = {"slug":("title",)}
    search_fields = ('title','description',)
    list_filter = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)