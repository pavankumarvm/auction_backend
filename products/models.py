import os
import uuid
from django.db import models
from django.db.models.base import Model

from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

from bids.models import Bid

# Create your models here.


def _delete_file(path):
    # Deletes file from filesystem.
    if os.path.isfile(path):
        os.remove(path)


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    code = models.CharField(max_length=5, null=False, blank=False)
    product_count = models.IntegerField(null=False, default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Category"


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    category_id = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to="products/", null=False)
    desc = models.CharField(max_length=300, null=True)
    min_price = models.IntegerField(null=False, default=1)
    recent_bid = models.ForeignKey(
        to=Bid, on_delete=models.SET_NULL, null=True)
    bid_count = models.IntegerField(null=False, default=0)
    start_at = models.DateTimeField(null=False, blank=False)
    expires_at = models.DateTimeField(null=False, blank=False)

    class Meta:
        db_table = "Product"

    def __str__(self) -> str:
        return self.name

    def delete(self):
        self.image.delete()
        super(Product, self).delete()


@receiver(post_delete, sender=Product)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.image:
        _delete_file(instance.image.path)


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    sequence_no = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.product_id + "--> " + str(self.sequence_no)

    def delete(self):
        self.image.delete()
        super(ProductImage, self).delete()

    class Meta:
        db_table = "Image"


@receiver(post_delete, sender=ProductImage)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.image:
        _delete_file(instance.image.path)
