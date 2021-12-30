import uuid
from django.db import models
from django.db.models.base import Model

from accounts.models import User
# from products.models import Product


# Create your models here.

class Bid(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    # product_id = models.OneToOneField(Product, on_delete=models.SET_NULL)
    bid_price = models.IntegerField(null=False, default=1)
    is_highest = models.BooleanField(default=False)
