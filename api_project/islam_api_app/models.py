from django.db import models


class Fatwas(models.Model):
    title = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fatwas'
        verbose_name_plural = 'fatwas'