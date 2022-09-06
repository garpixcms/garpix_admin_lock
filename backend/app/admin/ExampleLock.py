from garpix_admin_lock.mixins import PageLockAdminMixin
from django.contrib import admin
from ..models import ExampleLock


@admin.register(ExampleLock)
class ExampleLockAdmin(PageLockAdminMixin, admin.ModelAdmin):
    lock_change_view = True
    lock_changelist_view = False
