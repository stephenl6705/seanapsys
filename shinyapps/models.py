from django.db import models

class ShinyGroup(models.Model):
    username = models.CharField(max_length=50,default='')
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class ShinyItem(models.Model):
    itemid = models.CharField(max_length=20,default='')
    name = models.CharField(max_length=50,default='')
    dirname = models.CharField(max_length=50,default='')
    group = models.ForeignKey(ShinyGroup, default=None)

    def __str__(self):
        return self.name
