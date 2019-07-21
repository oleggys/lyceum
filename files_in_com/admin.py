from django.contrib import admin

# Register your models here.
from files_in_com.models import codifier, dis_learning, other, training_file, result


class heirarhyAdmin(admin.ModelAdmin):
    list_filter = ('subject',)

admin.site.register(codifier, heirarhyAdmin)
admin.site.register(dis_learning, heirarhyAdmin)
admin.site.register(other)
admin.site.register(training_file, heirarhyAdmin)
admin.site.register(result)