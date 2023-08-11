from django.contrib import admin
from django.http.request import HttpRequest

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

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
