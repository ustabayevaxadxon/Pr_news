from django.db import models

# Create your models here.


class POST(models.Model):
    title = models.CharField(max_length=264)
    body = models.TextField()

    def __str__(self):
        return self.title
