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


class BuildingType(models.Model):
    """
    建物種別
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_residential = models.BooleanField(_('is_residential'), db_column='is_residential', default=False)
    is_building = models.BooleanField(_('is_building'), db_column='is_building', default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'building_type'
        ordering = ['priority', 'id']
        verbose_name = _('building_type')
        verbose_name_plural = _('building_types')

    @property
    def is_condominium(self):
        if self.id == 40:
            return True
        else:
            return False