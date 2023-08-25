from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=10)
    working = models.BooleanField(default=False)
    salary = models.IntegerField(default=0)

def __str__(self):
    return self.name

class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    testimonial=models.TextField()
    picture=models.ImageField(upload_to='testimonials/')
    rating=models.IntegerField(max_length=1)   

def __str__(self):
    return self.testimonial
    
