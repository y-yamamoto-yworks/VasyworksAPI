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


class GarageType(models.Model):
    """
    駐車場種別
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_exist = models.BooleanField(_('is_exist'), db_column='is_exist', default=False)
    is_free = models.BooleanField(_('is_free'), db_column='is_free', default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'garage_type'
        ordering = ['priority', 'id']
        verbose_name = _('garage_type')
        verbose_name_plural = _('garage_types')

    @property
    def is_paid(self):
        """有料"""
        if self.is_exist and not self.is_free:
            return True
        else:
            return False
