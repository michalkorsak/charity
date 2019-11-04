from django.conf import settings
from django.db import models
from django.db.models import CASCADE

'''
category of institution
'''


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        indexes = [models.Index(fields=['name'])]
        ordering = ['-name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


INSTITUTION_CHOICES = (
    ('1', 'fundacja'),
    ('2', 'organizacja pozarządowa'),
    ('3', 'zbiórka lokalna'),
)


"""
Institution model, many to many with Categories
"""


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=22, choices=INSTITUTION_CHOICES, default='1')
    categories = models.ManyToManyField(Category)

    class Meta:
        indexes = [models.Index(fields=['name'])]
        ordering = ['-name']
        verbose_name = 'institution'
        verbose_name_plural = 'institutions'

    def __str__(self):
        return self.name


"""
model store donation details in db
"""


class Donation(models.Model):
    quantity = models.PositiveSmallIntegerField
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=30)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField(auto_now_add=True)
    pick_up_time = models.TimeField(auto_now_add=True)
    pick_up_comment = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)


