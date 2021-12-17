from wsgiref.validate import validator

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from config import settings


class UserModel(AbstractUser):
    """User model"""
    password2 = models.CharField(max_length=40)
    surname = models.CharField(max_length=40, verbose_name="Фамилия", blank=True)
    photo = models.ManyToManyField("PhotoFile", null=True, blank=True)
    video = models.ManyToManyField("VideoFile", null=True, blank=True)
    comments = models.ManyToManyField("Comment", null=True, blank=True)
    hobbies = models.ManyToManyField("Hobbie", null=True, blank=True)


def user_directory_path(user, filename):
    return 'photo/user_{0}/{1}'.format(user.url, filename)

class PhotoFile(models.Model):
    """Photo file user"""
    title = models.CharField(max_length=30, verbose_name='Фото пользователя', blank=True)
    url = models.ImageField(upload_to=user_directory_path)


class VideoFile(models.Model):
    title = models.CharField(max_length=30, verbose_name='Видео пользователя', blank=True)
    url = models.FileField(upload_to='photo/%Y/%m/%d/%s'.format(user_directory_path))


class Hobbie(models.Model):
    title = models.CharField(max_length=40, blank=False, null=False, unique=True)
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