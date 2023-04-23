from django.db import models
from django.contrib.auth.models import User

class Commodity(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.farmer.username}'s {self.quantity} KG {self.name}"