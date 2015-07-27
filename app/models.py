# from django.db import models

# # Create your models here.
# class Address(models.Model):
#     name = models.CharField(max_length=32)
#     source = models.CharField(max_length=40)
#     destination = models.CharField(max_length=40)


# class Distance(models.Model):
# 	job =models.IntegerField(editable =False)
# 	dist = models.DecimalField(max_digits=10, decimal_places=3)


from django.db import models

class UploadFile(models.Model):
	file = models.FileField(upload_to='app/static/waypoints/images/%Y/%m/%d')
	email = email = models.EmailField(unique=True)
	first_name = models.CharField(max_length = 20)
class User(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	email = models.EmailField(unique=True)