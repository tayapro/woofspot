from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from .models import WoofspotEvent

@admin.register(WoofspotEvent)
class WoofspotEventAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'image_preview')
    search_fields = ['title', 'content']
    list_filter = ('location', 'event_date', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 150px; height: auto;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"


