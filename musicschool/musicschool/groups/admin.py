from django.contrib import admin
from django.db import models

# Register your models here.
from .models import (
    Article, 
    Category,
    Media, 
    MemberGroup,
    UserInformations
)


class MemberGroupAdmin(admin.ModelAdmin):
    list_display = ('id','name')


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','name')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title')


class UserInformationsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'get_firstname', 
        'get_lastname', 
        'phonenumber', 
        'adress'
    )
    def get_firstname(self, obj):
        if obj.user.first_name:
            return obj.user.first_name
        else:
            return ''
    def get_lastname(self, obj):
        if obj.user.last_name:
            return obj.user.last_name
        else:
            return ''


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Media, MediaAdmin)

admin.site.register(MemberGroup, MemberGroupAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserInformations, UserInformationsAdmin)
