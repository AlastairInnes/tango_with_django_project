from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ("category", "title", "url")

# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
