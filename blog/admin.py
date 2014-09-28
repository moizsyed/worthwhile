from django.contrib import admin
from blog.models import Entry, Category, Source
from django_markdown.admin import MarkdownModelAdmin


class EntryAdmin(MarkdownModelAdmin):
  prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}

class SourceAdmin(admin.ModelAdmin):
  pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Source, SourceAdmin)