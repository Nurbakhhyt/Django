from django.db import models

class Flat(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title