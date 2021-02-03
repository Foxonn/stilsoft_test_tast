from django.contrib import admin

from roles.models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)
    list_display = ['name']
    list_filter = ['name']
    fieldsets = (
        ('Role', {'fields': (
            'name',
            'permissions',
        )}),
    )
