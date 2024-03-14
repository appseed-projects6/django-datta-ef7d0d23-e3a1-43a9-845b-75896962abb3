# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Simlarare(models.Model):

    #__Simlarare_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Simlarare_FIELDS__END

    class Meta:
        verbose_name        = _("Simlarare")
        verbose_name_plural = _("Simlarare")


class Skola(models.Model):

    #__Skola_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    klass = models.CharField(max_length=255, null=True, blank=True)

    #__Skola_FIELDS__END

    class Meta:
        verbose_name        = _("Skola")
        verbose_name_plural = _("Skola")


class Elev(models.Model):

    #__Elev_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    klass = models.CharField(max_length=255, null=True, blank=True)
    kunskap = models.CharField(max_length=255, null=True, blank=True)

    #__Elev_FIELDS__END

    class Meta:
        verbose_name        = _("Elev")
        verbose_name_plural = _("Elev")


class Termin(models.Model):

    #__Termin_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Termin_FIELDS__END

    class Meta:
        verbose_name        = _("Termin")
        verbose_name_plural = _("Termin")


class Kunskap(models.Model):

    #__Kunskap_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Kunskap_FIELDS__END

    class Meta:
        verbose_name        = _("Kunskap")
        verbose_name_plural = _("Kunskap")



#__MODELS__END
