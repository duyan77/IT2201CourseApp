from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/%Y/%m', null=True)

class BaseModels(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True
        ordering = ['-id']


class Category(BaseModels):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Course(BaseModels):
    subject = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)


class Meta:
    unique_together = ('subject', 'category')

    def __str__(self):
        return self.subject
