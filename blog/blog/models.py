from django.db import models

from django.urls import reverse

# Create your models here.

class Post(models.Model):# defining the columns that will be created in the sqllite db
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('post_detail', args = (str(self.id))) #after Post entry is added to db by model, post_detail url-view is the location to go to. see post detail url definition to see why self.id is necessary