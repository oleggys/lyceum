from django.contrib import admin
from documents.models import plat_documents, gos_document,license_document,provision_document,provisions,ruls_document,certificate_document,charter_document,internal_document,order_document,order_exec_document,other_document,pred_org_document,prokurat_document
# Register your models here.


class heirarhyAdmin(admin.ModelAdmin):
    list_filter = ('provision',)

admin.site.register(gos_document)
admin.site.register(license_document)
admin.site.register(provision_document, heirarhyAdmin)
admin.site.register(provisions)
admin.site.register(plat_documents)
admin.site.register(ruls_document)
admin.site.register(certificate_document)
admin.site.register(charter_document)
admin.site.register(internal_document, heirarhyAdmin)
admin.site.register(order_document)
admin.site.register(order_exec_document)
admin.site.register(other_document)
admin.site.register(pred_org_document)
admin.site.register(prokurat_document)