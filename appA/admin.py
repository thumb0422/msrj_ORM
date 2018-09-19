from django.contrib import admin
from .models import Photos

admin.site.site_header = '登录'

admin.site.site_title = '用户登录title'

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
