from .abstract import AbstractProduct, models

class WiredMicrophone(AbstractProduct):
    #size
    diameter  = models.PositiveSmallIntegerField(default=0)
    length    = models.PositiveSmallIntegerField(default=0)

    #properties
    diaphragm_type        = models.CharField(max_length=32)
    polar_pattern         = models.CharField(max_length=32)
    polar_pattern_switch  = models.BooleanField(default=False)
    on_off_switch         = models.BooleanField(default=False)
    require_phantom_power = models.BooleanField(default=False)
    cable_detached        = models.BooleanField(default=True)
    connection_type       = models.CharField(max_length=16) # default='XLR'
    impedance             = models.PositiveSmallIntegerField(default=0)
    color                 = models.CharField(max_length=32)

    #mics
    manual_url = models.URLField(default='')
    warranty_years = models.PositiveSmallIntegerField(default=2)