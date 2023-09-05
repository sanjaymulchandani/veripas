from django.db import models


# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or self.email
    
class HomeContent(models.Model):
    title = models.TextField()
    desctiption = models.TextField()
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title

class WebsiteLogo(models.Model):
    image = models.ImageField(upload_to='uploads/')
    
    def __str__(self):
        return self.image