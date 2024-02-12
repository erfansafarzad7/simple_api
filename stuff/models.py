from django.db import models


class Stuff(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
