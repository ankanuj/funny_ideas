from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_photo = models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_published=models.BooleanField(default=True)
    

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    heading = models.CharField(max_length=200,blank=True)
    content = models.CharField(max_length=1000,blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_published=models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.heading


class Feedback(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=1000,blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.feedback

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    com_date = models.DateTimeField(default=datetime.now,blank=True)
    is_published=models.BooleanField(default=True)
    reply = models.ForeignKey('self',null=True,related_name='replies',blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    

class Debate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    is_published=models.BooleanField(default=True)
    comment = models.TextField(max_length=1500)
    side = models.CharField(max_length=50,default='defence')
    com_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.topic

