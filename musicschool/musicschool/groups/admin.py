from django.contrib import admin

# Register your models here.
from musicschool.groups.models import Media, Article, MemberGroup

class MemberGroupAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    readonly_fields = ('image_tag',)

class Articledmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(MemberGroup, MemberGroupAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Article, Articledmin)