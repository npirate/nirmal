from django.contrib import admin

# Register your models here.

from .models import Patient, Visit

class VisitDetailInLine (admin.TabularInline):
    model = Visit

class PatientAdmin (admin.ModelAdmin):
    inlines = [
        VisitDetailInLine,
    ]

admin.site.register(Patient, PatientAdmin)
admin.site.register(Visit)
