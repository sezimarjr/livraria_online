from django.contrib import admin
from livraria import models

# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'author', 'price', 'publish_date',
    search_fields = 'title', 'author__name',
    list_per_page = 20
    ordering = '-id',
    list_max_show_all = 200
    list_display_links = 'id', 'title',


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'name',
    search_fields = 'name',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    search_fields = 'name',
