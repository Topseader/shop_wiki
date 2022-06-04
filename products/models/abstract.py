from django.db import models
from .brand import Brand

class AbstractProduct(models.Model):
    title      = models.CharField("Title", max_length=128)
    decription = models.TextField("Decription", blank=True)
    sku        = models.SlugField("SKU", max_length=7)
    brand      = models.ForeignKey(Brand, 
                                   models.SET_NULL,
                                   blank=True,
                                   null=True)

    def __str__(self):
        return f"{self.brand} {self.title}"

    class Meta:
    	abstract = True
