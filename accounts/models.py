from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  is_verified = models.BooleanField(default=False)
  auth_token = models.CharField(max_length=100, default = "12345")

  def __str__(self):
    return self.user.username

  @receiver(post_save, sender=User)
  def create_user_post_save_receiver(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile_post_save_receiver(sender, instance, created, **kwargs):
    instance.profile.save()

