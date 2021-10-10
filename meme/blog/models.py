from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    image= models.ImageField(default='default.jpg', upload_to='user_memes')
    date_posted= models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    #memer =models.ManyToOneField(Profile, on_delete=models.CASCADE, related_name="memer_id")
    likes=models.ManyToManyField(User, related_name='Likes', blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    def total_likes(self):
        return self.likes.count()

'''
class Comments(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    usr=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True)
    reply=models.ForeignKey('Comments',null='True', related_name='replies', on_delete=models.CASCADE)
    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.usr.username))
        '''