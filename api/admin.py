from django.contrib import admin
from api.models import *


# Register your models here.

@admin.register(Post)
class PostAdminView(admin.ModelAdmin):
    list_display = ['title', 'body', 'user',]


@admin.register(Tag)
class TagAdminView(admin.ModelAdmin):
    list_display = ['id', 'title']
