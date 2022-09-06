# Garpix Admin lock

Garpix Admin lock allows you to lock a page in the admin panel

## Quickstart

Install with pip:

```bash
pip install garpix_admin_lock
```

Add the `garpix_admin_lock` and dependency packages to your `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'garpix_admin_lock',
    # ...
]
```

Package not included migrations, set path to migration directory. Don't forget create this directory (`app/migrations/garpix_admin_lock/`) and place empty `__init__.py`:

```
app/migrations/
app/migrations/__init__.py  # empty file
app/migrations/garpix_admin_lock/__init__.py  # empty file
```

Add path to settings:

```python
# settings.py

MIGRATION_MODULES = {
    'garpix_admin_lock': 'app.migrations.garpix_admin_lock',
}
```

Add url to `urls.py`

```python
# url.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('page_lock/', include('garpix_admin_lock.urls')),
]

```

Run make migrations:

```bash
python manage.py makemigrations
```

Migrate:

```bash
python manage.py migrate
```

### Example

Add `PageLockViewMixin` in models

```python
# example/models.py
from django.db import models
from admin_page_lock.mixins import PageLockViewMixin


class ExampleLock(PageLockViewMixin, models.Model):
    ...
```

Add `PageLockAdminMixin` in admin

```python
# example/admin.py
from admin_page_lock.mixins import PageLockAdminMixin
from django.contrib import admin
from .models import Example

@admin.register(ExampleLock)
class ExampleAdmin(PageLockAdminMixin, admin.ModelAdmin):
    lock_change_view = True
    lock_changelist_view = False
    ...
```

### Basis

[django-admin-page-lock](https://github.com/Showmax/django-admin-page-lock)