from django.db import models
from django.urls import reverse

# Create your models here.

class Face(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  hotness = models.CharField(max_length=100)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("detail", kwargs={"face_id": self.pk})
  

