from django.db import models


# Create your models here.
class doner(models.Model):
	name=models.CharField(max_length=20)
	blood_type=models.CharField(max_length=20)
	phone_no=models.CharField(max_length=10,primary_key=True)
	address=models.CharField(max_length=50)


class reciever(models.Model):
	name=models.CharField(max_length=20)
	blood_type=models.CharField(max_length=20)
	phone_no=models.CharField(max_length=10,primary_key=True)
	address=models.CharField(max_length=50)