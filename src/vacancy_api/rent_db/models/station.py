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
from .railway import Railway
from lib.convert import *
from lib.functions import *


class Station(models.Model):
    """
    駅
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)

    railway = models.ForeignKey(
        Railway,
        db_column='railway_id',
        related_name='railway_stations',
        db_index=True,
        on_delete=models.PROTECT,
    )

    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_trading = models.BooleanField(_('is_trading'), db_column='is_trading', db_index=True, default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    transfer_stations = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='transfer_station_stations',
        through='TransferStation',
    )

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'station'
        ordering = ['priority', 'id']
        verbose_name = _('station')
        verbose_name_plural = _('stations')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)


class TransferStation(models.Model):
    """
    乗換駅
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)

    station = models.ForeignKey(
        'Station',
        db_column='station_id',
        related_name='station_transfer_stations',
        db_index=True,
        on_delete=models.PROTECT,
    )

    transfer_station = models.ForeignKey(
        'Station',
        db_column='transfer_station_id',
        related_name='transfer_station_transfer_stations',
        db_index=True,
        on_delete=models.PROTECT,
    )

    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'transfer_station'
        ordering = ['station_id', 'id']
        verbose_name = _('transfer_station')
        verbose_name_plural = _('transfer_stations')


