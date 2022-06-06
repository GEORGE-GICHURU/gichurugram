from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Follower
from homepage.models import Like, Comment, Post, PostImage
from directmessages.models import Message
# from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
import random


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_follower(sender, instance, created, **kwargs):
    gichurugramMainUser = User.objects.get(id=1)
    if created:
        Follower.objects.create(follower=instance, being_followed=instance)
        if not instance.pk == 1:
            Follower.objects.create(follower=instance, being_followed=gichurugramMainUser)
            Follower.objects.create(follower=gichurugramMainUser, being_followed=instance)
# creates a follower object so upon account creation, user is following my account and themselves.


@receiver(post_save, sender=User)
def create_objects(sender, instance, created, **kwargs):
    gichurugramMainUser = User.objects.get(id=1)
    randomImageArray = ['random_image/image1.jpg', 'random_image/image2.jpg', 'random_image/image3.jpg', 'random_image/image4.jpg', 'random_image/image5.jpg', 'random_image/image6.jpg', 'random_image/image7.jpg', 'random_image/image8.jpg', 'random_image/image9.jpg', 'random_image/image10.jpg']
    randomImage1 = random.choice(randomImageArray)
    randomImage2 = random.choice(randomImageArray)
    randomImage3 = random.choice(randomImageArray)

    if created:
        Message.objects.create(sender=gichurugramMainUser, receiver=instance, content='This is your inbox! Click me to view our conversation.')
        Post.objects.create(author=instance, caption='This is an autogenerated post to help you see the sites functions right away')
        post = Post.objects.get(author=instance, caption='This is an autogenerated post to help you see the sites functions right away')
        PostImage.objects.create(post=post, modelimage=randomImage1)
        PostImage.objects.create(post=post, modelimage=randomImage2)
        PostImage.objects.create(post=post, modelimage=randomImage3)
        Comment.objects.create(post=post, author=gichurugramMainUser, content='Here is your first comment!')


@receiver(pre_delete, sender=Like)
@receiver(pre_delete, sender=Comment)
@receiver(pre_delete, sender=Message)
@receiver(pre_delete, sender=Follower)
def delete_notifications(sender, instance, **kwargs):
    qs = delete_notifications.objects.get(target_object_id=instance.pk, target_content_type=ContentType.objects.get_for_model(instance))
    qs.delete()


# broke on initially letting people use it. Someone tried to submit a comment over 255. It through a 500 error, comment still created, but no notification. When i tried to delete a user whose pictures was commented on it threw a 500 error coudl not find notfcaiton for query. so i took out the notiofcation deletion code above. Shouldnt be too detrimental but should fix.