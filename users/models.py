from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    INN = models.CharField(max_length=14)

    is_beneficiary = models.BooleanField(default=False)


class Queue(models.Model):
    # is_beneficiary = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='Users')
    queue_list = models.ManyToManyField(Users)


class Operator(Users):
    Queue = models.OneToOneField('queue', on_delete=models.CASCADE, related_name='Queue')
    is_active = models.BooleanField(default=True)
