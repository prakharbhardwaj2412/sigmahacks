from django.db import models
from registration.models import user, shopkeeper


# Create your models here.
class shoppinglist(models.Model):
    pt = models.ForeignKey('user.name', on_delete="DO_NOTHING", null = True)
    shp = models.ForeignKey('shopkeeper.name', on_delete="DO_NOTHING", null = True)
    item = models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True,blank=True)
    # key=models.ForeignKey('',models.DO_NOTHING)
    Status=models.CharField(max_length=20,default="pending")