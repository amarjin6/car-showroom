from django.db import models


class ModelProperties(models.Model):
    is_active = models.BooleanField(default=False)
    last_update = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        abstract = True