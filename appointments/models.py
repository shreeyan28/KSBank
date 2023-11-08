from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    reason = models.TextField()
    time = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=255, default='123 Main Street')

    def __str__(self):
        return f"{self.name} - {self.email} - {self.age} - {self.reason} - {self.time} - {self.bank_address}"

from django.contrib.auth.models import AbstractUser
from django.db import models

class BankUser(AbstractUser):
    # Exclude default date_joined field
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # Add any additional fields you require
    email = models.EmailField(unique=True)

    class Meta:
        default_related_name = 'bankusers'

    # To avoid clashes with auth.User groups and permissions
    groups = models.ManyToManyField('auth.Group', related_name='bankuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='bankuser_set', blank=True)
