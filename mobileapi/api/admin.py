from django.contrib import admin

from .models import Worker, Unit, Visit


@admin.register(Worker)
class _Worder(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Unit)
class _Unit(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Visit)
class _Visit(admin.ModelAdmin):
    search_fields = ('unit__name', 'unit__worker__name')
