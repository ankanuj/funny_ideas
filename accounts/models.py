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
