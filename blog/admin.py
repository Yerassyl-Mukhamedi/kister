from django.contrib import admin
from .models import *

admin.site.register(Dogovor)
admin.site.register(Entity)
admin.site.register(Upload)
admin.site.register(OwnCompany)
admin.site.register(Sub)

class DogovorAdmin(admin.ModelAdmin):
    readonly_fields=('status')