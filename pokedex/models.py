from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    
    def __str__(self) -> str:
        return self.name
    
class Trainer(models.Model):
    first_name = models.CharField(30, null=False)
    last_name = models.CharField(30, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(default=1)