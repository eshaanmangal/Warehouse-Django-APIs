from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=True)
    contact_person_name = models.CharField(max_length=50, null=False, blank=False)