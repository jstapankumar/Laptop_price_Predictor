from django.db import models
'''
Company	TypeName	Ram	Weight	Price	Touchscreen	Ips	ppi	Cpu brand	HDD	SSD	Gpu brand	os
0	Apple	Ultrabook	8	1.37	71378.6832	0	1	226.983005	Intel Core i5	0	128	Intel	Mac
'''
# Create your models here.
class Laptop(models.Model):
    Company = models.CharField(max_length=100)
    TypeName = models.CharField(max_length=100)
    Ram = models.IntegerField()
    Weight = models.FloatField()
    Touchscreen = models.IntegerField()
    Ips = models.IntegerField()
    ppi = models.IntegerField()
    Cpu_brand = models.CharField(max_length=100)
    HDD = models.IntegerField()
    SSD = models.IntegerField()
    Gpu_brand = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    
    def __str__(self):
        return self.brand + ' ' + self.model
    
    
