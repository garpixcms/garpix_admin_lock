from django.db import models
from garpix_admin_lock.mixins import PageLockViewMixin


class ExampleLock(PageLockViewMixin, models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = "Пример"
        verbose_name_plural = "Примеры"
