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


class RoomStatus(models.Model):
    """
    部屋状況
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    for_rent = models.BooleanField(_('for_rent'), db_column='for_rent', default=False)
    is_pending = models.BooleanField(_('is_pending'), db_column='is_pending', default=False)
    will_be_canceled = models.BooleanField(_('will_be_canceled'), db_column='will_be_canceled', default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'room_status'
        ordering = ['priority', 'id']
        verbose_name = _('room_status')
        verbose_name_plural = _('room_statuses')
