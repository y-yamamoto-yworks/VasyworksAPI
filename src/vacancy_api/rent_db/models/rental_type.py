"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class RentalType(models.Model):
    """
    賃貸種別
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    short_name = models.CharField(_('short_name'), db_column='short_name', max_length=50, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_residential = models.BooleanField(_('is_residential'), db_column='is_residential', default=False)
    is_non_residential = models.BooleanField(_('is_non_residential'), db_column='is_non_residential', default=False)
    is_land = models.BooleanField(_('is_land'), db_column='is_land', default=False)
    is_limited_rent = models.BooleanField(_('is_limited_rent'), db_column='is_limited_rent', default=False)
    is_sublease = models.BooleanField(_('is_sublease'), db_column='is_sublease', default=False)
    is_own = models.BooleanField(_('is_own'), db_column='is_own', default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'rental_type'
        ordering = ['priority', 'id']
        verbose_name = _('rental_type')
        verbose_name_plural = _('rental_types')

