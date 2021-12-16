from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

def user_path(user, filename):
    return 'user_{0}/{1}'.format(user.username)



class UserModel(AbstractUser):
    """User model"""
    surname = models.CharField(max_length=40, verbose_name="Фамилия", blank=True)
    photo = models.ForeignKey("PhotoFile", on_delete=models.PROTECT, null=True, blank=True)
    video = models.ForeignKey("VideoFile", on_delete=models.PROTECT, null=True, blank=True)
    hobbies = models.ForeignKey("Hobbie", on_delete=models.PROTECT, null=True, blank=True)
    comments = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True, blank=True)


class PhotoFile(models.Model):
    """Photo file user"""
    title = models.CharField(max_length=30, verbose_name='Фото пользователя', blank=True)
    url = models.ImageField(upload_to='photo/%Y/%m/%d/{username}'.format(username=user_path))



class VideoFile(models.Model):
    title = models.CharField(max_length=30, verbose_name='Видео пользователя', blank=True)
    url = models.FileField(upload_to='photo/%Y/%m/%d/{username}'.format(username=user_path))


class Hobbie(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False)
    discription = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    user = models.ForeignKey(UserModel, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(UserModel, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False)
    discription = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False)
    discription = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

class News(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False)
    discription = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)