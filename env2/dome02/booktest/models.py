from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyUser(User):
    telephone = models.CharField(max_length=11)






class VoteInfo1(models.Model):
    title= models.CharField(max_length=50)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title


class VoteInfo2(models.Model):
    name = models.CharField(max_length=10)
    option = models.IntegerField(default=0)
    titles = models.ForeignKey(VoteInfo1, on_delete=models.CASCADE)
    def __str__(self):
        return self.name