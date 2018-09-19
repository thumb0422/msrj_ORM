from django.contrib import admin
from .models import Profile

admin.site.site_header = '登录'

admin.site.site_title = '用户登录title'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture')
