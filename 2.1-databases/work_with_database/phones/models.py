import datetime
from django.db import models
from django.forms import DateField, BooleanField, SlugField
from pytils.translit import slugify

class Phone(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    image = models.URLField(max_length = 200)
    release_date = models.DateField(default=datetime.date.today)
    lte_exists = models.BooleanField(default=False)
    slug = models.CharField(max_length = 50, default='')

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #         return super().save(*args, **kwargs)
