from os import truncate
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# from notifications.signals import notify
from django.utils.text import Truncator
from cloudinary.models import CloudinaryField

class Post(models.Model):
    caption = models.CharField(max_length=2200, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.caption


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    modelimage = CloudinaryField('images')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=500, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        n = 4
        truncatewords = Truncator(self.content).words(n)
        # notify.send(self.author, recipient=self.post.author, verb='commented' + truncatewords + 'on your post!', action_object=self.post, description='comment', target=self)


class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    date_created = models.DateTimeField(default=timezone.now)


    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)
        # notify.send(self.liker, recipient=self.post.author, verb='liked your post!' action_object=self.post, description='like', target=self)
