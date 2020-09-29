from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Assignment(models.Model):
    student_cid = models.CharField(max_length=15)
    teacher_cid = models.CharField(max_length=15)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cid = models.TextField(max_length=15, blank=True, default="")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Category_template(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.pk} : {self.name}"


class Descriptor_template(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.pk} : {self.name}"


class Record(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    student_cid = models.CharField(max_length=15)
    date = models.DateField(default=datetime.date.today)
    state = models.IntegerField(default=0)
    levels = models.CharField(max_length=200)
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")


class Record_category(models.Model):
    template = models.ForeignKey(Category_template, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    draft_level = models.IntegerField(default=0)
    feedback_level = models.IntegerField(default=0)
    final_level = models.IntegerField(default=0)


class Record_descriptor(models.Model):
    template = models.ForeignKey(Descriptor_template, on_delete=models.CASCADE)
    category = models.ForeignKey(Record_category, on_delete=models.CASCADE)
    draft_level = models.IntegerField(default=0)
    feedback_level = models.IntegerField(default=0)
    final_level = models.IntegerField(default=0)
    draft_statement = models.TextField(default="")
    feedback_statement = models.TextField(default="")
    final_statement = models.TextField(default="")