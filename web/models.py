from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __str__(self):
        return '{}_Token'.format(self.user)

# we create a model here for outcoming money / contains--> text-date-amount-user
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # this function will change the name of table into the exact date and time and amount
    def __str__(self):
        return "{}-{}".format(self.date, self.amount)


# another model for incoming money
class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # this function will change the name of table into the exact date and amount
    def __str__(self):
        return "{}-{}".format(self.date, self.amount)