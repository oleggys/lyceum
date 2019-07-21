from django.contrib import admin

# Register your models here.
from offer_and_com.models import offer,complaint


class offerAdmin(admin.ModelAdmin):
    list_display = ('topic', 'name', 'email', 'phone')
    inlines = []

admin.site.register(offer, offerAdmin)
admin.site.register(complaint, offerAdmin)