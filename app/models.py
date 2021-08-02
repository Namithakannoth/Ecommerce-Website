from django.db import models

from django.urls import reverse
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20,null=True)
    description=models.TextField(null=True)
    originalPrice=models.IntegerField(null=True)
    discountedPrice=models.IntegerField(null=True)
    image=models.CharField(max_length=200,null=True)
    slug = models.SlugField(max_length=100, null=True)


    def get_absolute_url(self):
        return reverse("hello", kwargs={"slug": self.slug})

class Checkout(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emailId = models.CharField(max_length=50)
    phoneNo = models.IntegerField()
    price = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=40)
    pincode = models.IntegerField()
    address = models.TextField()

class Contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emailId = models.CharField(max_length=50)
    phoneNo = models.IntegerField()
    query = models.TextField()