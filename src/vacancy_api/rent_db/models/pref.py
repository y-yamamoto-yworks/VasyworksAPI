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
from lib.functions import *


class Pref(models.Model):
    """
    都道府県
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_trading_area = models.BooleanField(_('is_trading_area'), db_column='is_trading_area', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pref'
        ordering = ['priority', 'id']
        verbose_name = _('pref')
        verbose_name_plural = _('prefs')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)
