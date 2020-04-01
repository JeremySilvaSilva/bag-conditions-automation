from django.contrib import admin
from .models import (
    Factor,BodyTag,
    FactorBodyTag
)

class FactorBodyTagInline(admin.TabularInline):
    model = FactorBodyTag

class FactorAdmin(admin.ModelAdmin):
    inlines = [
        FactorBodyTagInline,
    ]

admin.site.register(Factor,FactorAdmin)
admin.site.register(BodyTag)
admin.site.register(FactorBodyTag)