from django.db import models
from django_countries.fields import CountryField


class ShowRoom(AbstractModel):
    name = models.CharField(max_length=30)
    location = CountryField(blank_label='(select country)')
    customers = models.TextField(default='')
    history = models.TextField(default='')

    def __str__(self):
        return self.name
