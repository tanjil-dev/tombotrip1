from django.db import models
from datetime import datetime
from ckeditor.fields import  RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
# Create your models here.
class Traveller(models.Model):
    overview = RichTextUploadingField()
    def __str__(self):
         return self.overview
class Ownercamper(models.Model):
    ownercamper = RichTextUploadingField()
    ownercaravan = RichTextUploadingField()
    def __str__(self):
         return self.ownercamper
class Ownercaravan(models.Model):
    overview = RichTextUploadingField()
    def __str__(self):
         return self.overview         
class Faq(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,blank=True)
    overview = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name    

class Ownerquote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True,upload_to='photos/%Y/%m/%d/')
    quote = models.TextField()
    job_position = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username