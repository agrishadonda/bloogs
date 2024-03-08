from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    tital = models.CharField(max_length = 15)
    content = models.TextField()
    date_posted = models.DateField(default = timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.tital
    
    def get_absolute_url(self):
        return reverse("detail",kwargs = {'pk':self.pk})
    
