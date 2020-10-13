"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lib.convert import *
from lib.functions import *


class Railway(models.Model):
    """
    鉄道沿線
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    short_name = models.CharField(_('short_name'), db_column='short_name', max_length=50, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_trading = models.BooleanField(_('is_trading'), db_column='is_trading', db_index=True, default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'railway'
        ordering = ['priority', 'id']
        verbose_name = _('railway')
        verbose_name_plural = _('railways')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)

