from .abstract import AbstractProduct, models

class WiredMicrophone(AbstractProduct):
    #size
    diameter  = models.PositiveSmallIntegerField("Diameter", default=0)
    length    = models.PositiveSmallIntegerField("Length", default=0)

    #properties
    diaphragm_type        = models.CharField("Diaphragm type", 
                                             max_length=32)
    polar_pattern         = models.CharField("Polar pattern",
                                             max_length=32)
    polar_pattern_switch  = models.BooleanField("Polar pattern switch",
                                                default=False)
    on_off_switch         = models.BooleanField("On-off switch", 
                                                default=False)
    require_phantom_power = models.BooleanField("Require phantom power", 
                                                default=False)
    cable_detached        = models.BooleanField("Cable detached", 
                                                default=True)
    connection_type       = models.CharField("Connection type", 
                                             max_length=16)
    impedance             = models.PositiveSmallIntegerField("Impedance", 
                                                             default=0)
    color                 = models.CharField("Color", 
                                             max_length=32)

    #mics
    manual_url = models.URLField("Manual URL", default='')
    warranty_years = models.PositiveSmallIntegerField("Warranty years", default=2)