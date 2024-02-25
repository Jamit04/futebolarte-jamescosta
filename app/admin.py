from django.contrib import admin
from .models import Clube

# Register your models here.
@admin.register(Clube)
class ClubeSdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado', 'cores', 'ano_fundacao', 'tem_mundial')

    list_filter = ('nome', 'estado')

    search_fields = ('nome', 'estado','cores')