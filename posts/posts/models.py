from django.db import models

# Create your models here.
class Post (models.Model):
    text = models.TextField()

    def __str__ (self): #we are adding __str__ method to our model class. This is a good practise
        return self.text[:50]