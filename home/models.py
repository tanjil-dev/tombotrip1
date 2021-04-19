from django.db import models
from ckeditor.fields import  RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from django.forms import ModelForm
from django.db.models import Avg, Count
import datetime
from django.forms import ModelForm
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.html import mark_safe
# Create your models here.

class Experience(models.Model):
    title_keyword = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    overview = RichTextUploadingField()
    image = models.ImageField(blank=True,null=True,upload_to='photos/%Y/%m/%d/')
    title1 = models.CharField(max_length=100)
    overview1 = RichTextUploadingField()
    image1 = models.ImageField(blank=True,null=True,upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title_keyword

    def get_absolute_url(self):
        return reverse('exp-details', kwargs={
            'slug': self.slug
        })    
class Cartypes(models.Model):
    title = models.CharField(max_length=20)
    image=models.ImageField(blank=True,null=True, upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title
class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Transmission(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
class Supply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cartypes  = models.ManyToManyField(Cartypes)
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=False, unique=True)
    car_title =  models.CharField(max_length=150)
    city =  models.CharField(max_length=150)
    price =  models.IntegerField()
    main_photo =  models.ImageField(upload_to='photos/%Y/%m/%d/') 
    image1 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image2 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image3 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image4 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image5 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image6 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image7 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image8 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image9 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image10 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image11 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image12 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image13 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image14 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image15 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image16 =  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image17=  models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    seats =  models.IntegerField()
    bearth =  models.IntegerField()
    features = RichTextUploadingField()
    description = RichTextUploadingField()
    failities = RichTextUploadingField() 
    houserules = RichTextUploadingField()
    min_reserver_period = models.IntegerField()
    pick_up_from = models.TimeField(blank=True)
    drop_of_before = models.TimeField(blank=True)
    favourite = models.ManyToManyField(User,related_name='favourite',blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('/home')    
    def avaregereview(self):
        reviews = Rating.objects.filter(supply=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Rating.objects.filter(supply=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt        
    # def get_absolute_url(self):
    #     return reverse('/home', kwargs={
    #         'slug': self.slug
    #     })   
    # def get_absolute_url(self):
    #     return reverse('supply-details',kwargs={'pk':self.pk})    
class ProductAttribute(models.Model):
    supply=models.ForeignKey(Supply,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.supply.title
class Rating(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    supply=models.ForeignKey(Supply,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='True')
    create_at=models.DateTimeField(default = timezone.now)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    supply=models.ForeignKey(Supply,on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    supply = models.ForeignKey(Supply, on_delete=models.DO_NOTHING)
    time = models.DateField()
    message = models.CharField(max_length=150)

class CommentForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['subject', 'comment', 'rate']
