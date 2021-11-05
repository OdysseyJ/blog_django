from django.utils import timezone
from django.db import models

from softdelete.models import SoftDeleteObject


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def touch(self):
        self.save(update_fields=[])

    def save(self,
             force_insert=False,
             force_update=False,
             using=None,
             update_fields=None):
        self.updated_at = timezone.now()
        if update_fields is not None:
            update_fields.append('updated_at')
        super(TimestampMixin, self).save(force_insert, force_update, using,
                                         update_fields)


class Model(SoftDeleteObject, TimestampMixin, models.Model):
    class Meta:
        abstract = True
