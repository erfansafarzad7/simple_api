from django.db import models


class Stuff(models.Model):
    owner = models.ForeignKey('auth.User', related_name='user_stuffs', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
