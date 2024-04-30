from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import StartUpType, Category, StartUp


# Register your models here.

@admin.register(StartUpType)
class StartUpTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'created', 'updated', 'published')
    list_display_links = ('pk', 'name')
    list_editable = ('published', )
    list_filter = ('published', 'created')

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'created', 'updated', 'published')
    list_display_links = ('pk', 'name')
    list_editable = ('published', )
    list_filter = ('created', 'updated')

    prepopulated_fields = {'slug': ('name',)}


@admin.register(StartUp)
class StartUpAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created', 'authors', 'category', 'published', 'get_image')
    list_display_links = ('pk', 'title')
    list_filter = ('category', 'created')
    list_editable = ('published', )

    prepopulated_fields = {'slug': ('title', 'category')}

    def get_image(self, startup):
        if startup.image:
            url = startup.image.url
        else:
            url = "https://media.istockphoto.com/id/1055079680/vector/black-linear-photo-camera-like-no-image-available.jpg?s=612x612&w=0&k=20&c=P1DebpeMIAtXj_ZbVsKVvg-duuL0v9DlrOZUvPG6UJk="
        return mark_safe(f'<img src="{url}" width="80">')

    get_image.short_description = "Image"
