from django.db import models
from ckeditor.fields import  RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
     
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
         
    def __str__(self):
        return self.title
class About(models.Model):
    title = models.CharField(max_length=100)
    overview = RichTextUploadingField()
    image = models.ImageField(blank=True,null=True,upload_to='photos/%Y/%m/%d/') 
    def __str__(self):
        return self.title

class Agents(models.Model):
    name =  models.CharField(max_length=100)
    job_position =  models.CharField(max_length=100)
    overview = RichTextUploadingField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
  
    
    def __str__(self):
        return self.name
class Easysafe(models.Model):
    title = models.CharField(max_length=100)
    overview = RichTextUploadingField()
    image = models.ImageField(blank=True,null=True,upload_to='photos/%Y/%m/%d/') 
    def __str__(self):
        return self.title
class Message(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.ImageField(blank=True,null=True,upload_to='photos/%Y/%m/%d/') 
    def __str__(self):
        return self.title
