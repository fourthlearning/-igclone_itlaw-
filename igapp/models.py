from django.db import models
# Create your models here.

class IGUser(models.Model):
    ig_username = models.CharField(max_length=255)
    # email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=255)
    fullname = models.TextField(null=True)

    

class Logined(models.Model):
    ig_username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class FBuser(models.Model):
    fb_username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    
    
    #username :admin // password:admin