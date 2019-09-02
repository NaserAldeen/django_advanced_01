from django.db import models
from stores.models import *
# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="inventories")
    is_empty = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    