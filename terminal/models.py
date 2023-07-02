from django.db import models

class PersonCategory(models.Model):
    name_category = models.CharField(
        max_length=50,
        verbose_name='Категория человека'
    )

class Service(models.Model):
    title = models.CharField(
        max_length=255
    )
    is_for_individuals = models.BooleanField(
        default=True
    )
    is_for_legal_entities = models.BooleanField(
        default=True
    )
