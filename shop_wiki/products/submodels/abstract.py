from django.db import models

class AbstractProduct(models.Model):
	title      = models.CharField(max_length=128)
    decription = models.TextField(blank=True)
    sku        = models.SlugField(max_length=7)
    brand      = models.ForeignKey(Brand, 
                                   models.SET_NULL,
                                   blank=True,
                                   null=True)

    def __str__(self):
        return f"{self.brand} {self.title}"

    class Meta:
    	abstract = True
