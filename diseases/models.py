from django.db import models
from datetime import datetime
from django.utils import timezone, timesince
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Thumbnail(models.Model):
  upload_date = models.DateTimeField(auto_now_add=True, auto_now=False)
  image = models.ImageField(upload_to="photos/%Y/%m/%d/")
  featured = models.BooleanField(default=True)
  diseaseName = models.CharField(max_length=50, default="unbound")
  user = models.ForeignKey(User, on_delete=CASCADE)

  def __str__(self) -> str:
      return str(self.id) + str(self.diseaseName)


class DiseaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(featured=True)


class Disease(models.Model):
  name = models.CharField(null=False, blank=False, max_length=50,)
  other_name_1 = models.CharField(null=True, blank=True, max_length=50)
  other_name_2 = models.CharField(null=True, blank=True, max_length=50)
  other_name_3 = models.CharField(null=True, blank=True, max_length=50)
  description = models.CharField(max_length=150, null=True, blank=True)
  differentials = models.ManyToManyField("self", blank=True)
  extra_information = models.CharField(max_length=1000, null=True, blank=True)
  aetiology = models.CharField(max_length=100)  
  link = models.URLField()
  view_count = models.IntegerField(default=0)
  featured = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True, auto_now=False)
  symptoms = models.CharField(max_length=200, blank=True, null=True)
  transmission = models.CharField(max_length=200, blank=True, null=True)
  thumbnail = models.ForeignKey(Thumbnail,  on_delete=CASCADE)


# change symptoms from blank = True to false


  def __str__(self) -> str:
      return self.name


class DiseaseImageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(verified=True).filter(featured=True)


class DiseaseImage (models.Model):
  disease = models.ForeignKey(Disease, on_delete=CASCADE)
  image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank = False, null = False )
  user = models.ForeignKey(User, on_delete=CASCADE)
  featured = models.BooleanField(default=False)
  verified = models.BooleanField(default=False)
  upload_date = models.DateTimeField(auto_now_add=True, auto_now=False)
  extra_information = models.CharField(default="no extra information", max_length=500, )

  def __str__(self) -> str:
      return str(self.id)

  def is_recently_added(self):
    return self.upload_date >= timezone.now() - datetime.timedelta(days=7)

  class Meta:
    ordering = ["-upload_date"]


# Create your models here.
