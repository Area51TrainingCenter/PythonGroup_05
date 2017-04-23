from django.contrib import admin

from actividades.models import Actividad, Lugar


class ActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'lugar', 'fecha',)
    list_display_links = ('titulo', 'lugar',)
    list_filter = ('lugar',)
    search_fields = ('titulo',)
    list_editable = ('fecha',)

admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Lugar)
