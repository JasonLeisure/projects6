from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse



# Create your models here.

class LocationVO(models.Model):
    href = models.CharField(max_length=300, null=True, blank=True, unique=True)
    closet_name = models.CharField(max_length=300)
    section_number = models.PositiveBigIntegerField()
    shelf_number = models.PositiveBigIntegerField()

class Hat(models.Model):
    fabric = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture_url = models.URLField(null=True, blank=True)
    location = models.ForeignKey(
        LocationVO,
        related_name="hats",
        on_delete=models.PROTECT,
    )
