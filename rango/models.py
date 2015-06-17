from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name