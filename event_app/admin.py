from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import WoofspotEvent

# Register your models here.
@admin.register(WoofspotEvent)
class WoofspotEventAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'content']
    list_filter = ('location', 'event_date', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'created_on')

