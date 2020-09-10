from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pisteet = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Tulokset(models.Model):
    ottelupari = models.CharField(max_length=100)
    tulos = models.CharField(max_length=5, blank=True)
    pelattu = models.BooleanField()

    def __str__(self):
        return self.ottelupari


class Veikkaukset(models.Model):
    osallistuja = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tulokset = models.ForeignKey(Tulokset, on_delete=models.CASCADE)
    veikkaus = models.CharField(max_length=5)

    def __str__(self):
        return self.veikkaus

