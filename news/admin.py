from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, News, Author


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category', 'is_published')
    summernote_fields = ('description',)
