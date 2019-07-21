from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from lyceum.models import Staff, positions, subject, Event, events_in_day, Lyceum_news, message


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'last_name')
    inlines = []


class messageAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'topic', 'text')
    inlines = []


class eventsInLine(admin.StackedInline):
    model = events_in_day
    extra = 2

class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'event_date'
    inlines = [eventsInLine]

admin.site.register(Event, EventAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(positions)
admin.site.register(Lyceum_news)
admin.site.register(subject)
admin.site.register(message, messageAdmin)

class AdminCategory(ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'active']
    list_filter = ('active',)

    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (('title', 'active'), 'parent')
        }),
        ('Preview', {
            'classes': ('suit-tab suit-tab-preview',),
            'fields': ('preview_image', 'preview_text')
        }),
        ('Detail', {
            'classes': ('suit-tab suit-tab-detail',),
            'fields': ('detail_image', 'detail_text')
        }),
        ('Seo', {
            'classes': ('suit-tab suit-tab-seo',),
            'fields': ('seo_keywords', 'seo_description')
        }),
    )

    suit_form_tabs = (('general', 'General'), ('preview', 'Preview'), ('detail', 'Detail'), ('seo', 'Seo'),)