from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cities'
        verbose_name = 'city'
        verbose_name_plural = 'cities'