from django.db import models

class Brand(models.Model):
    title = models.CharField("Title", max_length=64, default='')
    decription = models.TextField("Decription", default='')
    official_url = models.URLField("Official URL", default='')

    def __str__(self):
        return self.title