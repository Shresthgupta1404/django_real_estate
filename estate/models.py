from django.db import models

# Create your models here.
class desc(models.Model):
	keyword=models.CharField(max_length=100)
	types=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	bedrooms=models.CharField(max_length=100)
	garages=models.CharField(max_length=100)
	price=models.CharField(max_length=100)
	avatar=models.ImageField(null=True,upload_to="../img",default="../default_avatar.png")
