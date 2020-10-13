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
from .pref import Pref


class Area(models.Model):
    """
    エリア
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    kana = models.CharField(_('kana'), db_column='kana', db_index=True, max_length=100, null=True, blank=True)

    pref = models.ForeignKey(
        Pref,
        db_column='pref_id',
        related_name='pref_areas',
        db_index=True,
        on_delete=models.PROTECT,
    )

    lat = models.FloatField(_('lat'), db_column='lat', db_index=True, default=0)
    lng = models.FloatField(_('lng'), db_column='lng', db_index=True, default=0)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'area'
        ordering = ['pref_id', 'kana', 'id']
        verbose_name = _('area')
        verbose_name_plural = _('areas')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)
