from django.contrib import admin
from .models import Licenciatura

# Register your models here.
@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'ects')
    search_fields = ('nome', 'instituicao')
