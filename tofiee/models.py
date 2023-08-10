from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from django.utils.text import slugify
import uuid

# Create your models here.
class Member(models.Model):
  username = models.CharField(max_length=15, default='none')
  price = models.FloatField()
  title = models.CharField(max_length=25)
  region = models.CharField(max_length=25, default='none')
  city = models.CharField(max_length=25, default='none')
  description = models.CharField(max_length=1000, blank=True)
  date = models.DateTimeField(default=datetime.now())
  size = models.CharField(max_length=50, default='none', blank=True)
  contact = models.CharField(max_length=10, blank=True)
  dp = models.ImageField(upload_to='images/',default='default.jpg', blank=True)
  pic1 = models.ImageField(upload_to='images/',default='default.jpg', blank=True)
  pic2 = models.ImageField(upload_to='images/',default='default.jpg', blank=True)
  pic3 = models.ImageField(upload_to='images/',default='default.jpg', blank=True)
  pic4 = models.ImageField(upload_to='images/',default='default.jpg', blank=True)
  pic5 = models.ImageField(upload_to='images/',default='default.jpg', blank=True)
  pic6= models.ImageField(upload_to='images/',default='default.jpg', blank=True)
  rooms = models.FloatField(max_length=50)
  bathrooms = models.FloatField(max_length=50)
  utilities = models.CharField(max_length=100)
  category = models.CharField(max_length=100, default='none')
  active = models.CharField(max_length=10, default='0', blank=True)
  slug = models.SlugField(max_length=200, unique=True)
  newsletter = models.CharField(max_length=100, default=0)
  document_a = models.FloatField(max_length=100, default=0)
  document_b = models.FloatField(max_length=100, default=0)
  document_c = models.FloatField(max_length=100, default=0)
  def __str__(self):
    return self.username

  def save(self, *args, **kwargs):
    if not self.slug:
        unique_id = uuid.uuid4()
        slug = slugify(str(unique_id))
        self.slug = slug
    super().save(*args, **kwargs)
# Create your models here.
