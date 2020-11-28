from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS_CHOICES = [
    (0, 'Draft'),
    (1, 'Publish')
]

class Post(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES,default=0)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='users')
#     role = models.CharField(max_length=50)
#     mobile_number = models.IntegerField(unique=True)
#     address = models.CharField(max_length=250)

#     def __str__(self):
#         return self.role


