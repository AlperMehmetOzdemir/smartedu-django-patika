from django.db import models

# Create your models here.
class Teacher(models.Model):
  name = models.CharField(("Name"), max_length=50)
  title = models.CharField(("Title"), max_length=50)
  description = models.TextField(("Description"), blank=True)
  image = models.ImageField(("Profile picture"), upload_to="courses/%Y/%m/%d/")
  facebook = models.URLField(("Facebook profile URL"), max_length=200, blank=True)
  twitter = models.URLField(("Twitter profile URL"), max_length=200, blank=True)
  linkedin = models.URLField(("Linkedin profile URL"), max_length=200, blank=True)
  youtube = models.URLField(("Youtube profile URL"), max_length=200, blank=True)


  def __str__(self) -> str:
      return self.name