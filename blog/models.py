from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.forms import ModelForm
from django import forms
# Create your models here.
# author
# title/slug/author/description/image/date/featured/pre_post/next_post
# comment
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.user.username
class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('posts_in_category', kwargs={
            'slug': self.slug
        })
    
    def save(self, *args, **kwargs):
        if self.title:
            self.title = self.title.capitalize()

        super(Category, self).save(*args, **kwargs)            
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

   
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'slug': self.slug
        })
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies',on_delete=models.CASCADE)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body') 