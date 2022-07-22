from django.db import models


class AbstractModel(models.Model):
    is_active = models.BooleanField(default=False)
    last_update = models.DateTimeField()
    instance_time = models.TimeField()

    class Meta:
        abstract = True