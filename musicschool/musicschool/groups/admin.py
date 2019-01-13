from django.contrib import admin

# Register your models here.
from musicschool.groups.models import (
    Media, 
    Article, 
    MemberGroup, 
    UserInformations
)

class MemberGroupAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    readonly_fields = ('image_tag',)

class Articledmin(admin.ModelAdmin):
    list_display = ('id','title')

class UserInformationsdmin(admin.ModelAdmin):
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
        

admin.site.register(MemberGroup, MemberGroupAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Article, Articledmin)
admin.site.register(UserInformations, UserInformationsdmin)