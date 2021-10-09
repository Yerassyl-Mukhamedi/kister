from django.contrib import admin
from .models import *

admin.site.register(Dogovor)
admin.site.register(Entity)
admin.site.register(Upload)
admin.site.register(OwnCompany)
admin.site.register(Sub)
admin.site.register(InMail)
admin.site.register(OutMail)
admin.site.register(Worker)

class DogovorAdmin(admin.ModelAdmin):
    readonly_fields=('status')


class InMailAdmin(admin.ModelAdmin):
    readonly_fields=('status')

class OutMailAdmin(admin.ModelAdmin):
    readonly_fields=('status')