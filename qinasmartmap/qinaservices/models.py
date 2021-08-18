from django.db import models
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Hospital'


# Create your models here.
class Ambulance(models.Model):
    name = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Ambulance'


class PostOffice(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'PostOffice'


class Mosque(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Mosque'


class Church(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Church'


class FireStation(models.Model):
    name = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'FireStation'


class Kindergarten(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Kindergarten'


class PrimarySC(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'PrimarySC'


class PreparatorySC(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'PreparatorySC'


class HighSC(models.Model):
    name = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'HighSC'





