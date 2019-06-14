from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=5000)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
