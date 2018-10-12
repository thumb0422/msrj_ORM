from django.contrib import admin
from .models import Photos,Author,Publisher,Book

admin.site.site_header = '登录'

admin.site.site_title = '用户登录title'

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ('name', 'age','phone','email')
    # 添加搜索功能
    search_fields = ('name', 'age', 'phone', 'email')
    # 编辑的时候首先显示名字 年龄 邮箱 和手机号
    fields = ('name', 'age', 'email', 'phone')
    # 按照年龄排序
    ordering = ('age',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','website')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list_display = ('name', 'author','publisher','publication_date')
    list_display = ('name', 'publication_date',)
    # 显示关联的外健
    raw_id_fields = ('author', 'publisher',)
    # 显示过滤字段
    list_filter = ('author',)

from .models import Hero
from django.utils.safestring import mark_safe
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    # readonly_fields = ['headshot_image']
    #
    # def headshot_image(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url=obj.headshot.url,
    #         width=obj.headshot.width,
    #         height=obj.headshot.height,
    #     )
    #     )

    def upload_img(self, obj):
        try:
            img = mark_safe('''<a href="%s"><img src="%s" width="50px" /></a>''' % (obj.image.url, obj.image.url))
        except Exception as e:
            img = ''
        return img

    upload_img.short_description = 'Thumb'
    upload_img.allow_tags = True

    list_display = ['id', 'image', 'upload_img']
    readonly_fields = ['upload_img']