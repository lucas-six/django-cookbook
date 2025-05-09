"""Admin."""

from django.contrib import admin

from .models import A, B


@admin.register(A)
class AAdmin(admin.ModelAdmin):
    """A Admin"""

    list_display = (
        'id',
        'name',
        'nickname',
        'age',
        'balance',
        'score',
        'is_active',
        'created_time',
        'updated_time',
        'group',
        'remark',
    )
    list_editable = ['is_active']
    list_filter = ('is_active', 'updated_time', 'created_time')
    search_fields = ('name', 'uuid', 'nickname', 'group__name', 'remark')


@admin.register(B)
class BAdmin(admin.ModelAdmin):
    """B Admin"""

    list_display = (
        'id',
        'a',
    )
    list_editable = []
    list_filter = ()
    search_fields = ('a__name', 'a__uuid')
