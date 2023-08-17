from django.db import models

# Create your models here.
class PageView(models.Model):
    page_view = models.IntegerField()
    ip = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

class Service(models.Model):
    sname = models.CharField(max_length=75)
    slogo = models.CharField(max_length=255)
    sdesc = models.TextField(null=True, blank=True)

class Portfolio(models.Model):
    pname = models.CharField(max_length=75)
    pdesc = models.TextField()
    pimage = models.ImageField(blank=True, null=True, upload_to='portfolio')

class Member(models.Model):
    mname = models.CharField(max_length=100)
    designation = models.CharField(max_length=75)
    email = models.EmailField(max_length=75)
    phone = models.CharField(max_length=75)
    mimage = models.ImageField(default='member/default.png', upload_to='member', blank=True)

class Contact(models.Model):
    cname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

class IctResource(models.Model):
    rname = models.CharField(max_length=255)
    file = models.FileField(upload_to='doc', blank=True)