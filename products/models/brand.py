from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=64, default='')
    decription = models.TextField(default='')
    official_url = models.URLField(default='')

    def __str__(self):
        return self.title