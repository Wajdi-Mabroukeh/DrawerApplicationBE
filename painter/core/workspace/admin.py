import django
from django.contrib import admin

from core.workspace.models import WorkSpace


@django.contrib.admin.register(WorkSpace)
class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'uuid', )#'shapes')

    search_fields = ('uuid', 'title')
    ordering = ('-created_at',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return True