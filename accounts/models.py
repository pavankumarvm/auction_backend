import os
import uuid
from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

from .managers import UserManager
# Create your models here.


def _delete_file(path):
    # Deletes file from filesystem.
    if os.path.isfile(path):
        os.remove(path)


class User(AbstractBaseUser, PermissionsMixin):

    # Creates User
    user_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=35, unique=True, blank=False, null=False)
    photo = models.ImageField(
        upload_to="profile_photo/", default="profile_photo/avatar.png")
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    phone_no = models.CharField(max_length=10, blank=False, null=False)
    email = models.EmailField(
        max_length=50, blank=False, null=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_no']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True

    def delete(self):
        self.photo.delete()
        super(User, self).delete()

    class Meta:
        db_table = 'User'


@receiver(post_delete, sender=User)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.photo:
        _delete_file(instance.photo.path)


class Otp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    otp_valid_time = models.DateTimeField(auto_now_add=True)
    no_of_attempts = models.IntegerField(default=5)

    class Meta:
        db_table = "otp"
