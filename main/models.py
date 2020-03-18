from django.db import models

# Create your models here.
class destination(models.Model):
	name=models.CharField(max_length=50)
	desc=models.TextField(max_length=500)
	img=models.ImageField(upload_to='pics')
	price=models.IntegerField(default=0)
