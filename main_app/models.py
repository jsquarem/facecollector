from django.db import models
from django.urls import reverse

# Create your models here.



GENDER = (
  ('F', 'Female'),
  ('M', 'Male'),
  ('N', 'Non-Binary'),
  ('R', 'Rather Not Say')
)

class Face(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  hotness = models.CharField(max_length=100)
  date = models.DateTimeField(auto_now_add=True)
  gender = models.CharField(
    max_length = 1,
    choices = GENDER,
    default = GENDER[2][0]
  )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("detail", kwargs={"face_id": self.pk})
  
class Picture(models.Model):
  date = models.DateField(auto_now_add=True)
  url = models.URLField(max_length=200)
  face = models.ForeignKey(Face, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.id} on {self.date}"

  class Meta:
    ordering = ['-date']
