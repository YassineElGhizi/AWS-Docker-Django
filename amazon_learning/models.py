from django.db import models

from my_amazon_learning.models import TimeStamped


# Create your models here.
class Note(TimeStamped):
    note = models.TextField()
    image = models.ImageField(upload_to="note_images/", null=True, blank=True)
