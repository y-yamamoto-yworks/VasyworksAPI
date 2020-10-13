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
from .landmark_type import LandmarkType


class Landmark(models.Model):
    """
    ランドマーク
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)

    landmark_type = models.ForeignKey(
        LandmarkType,
        db_column='landmark_type_id',
        related_name='landmark_type_landmarks',
        db_index=True,
        on_delete=models.PROTECT,
    )
    
    name = models.CharField(_('name'), db_column='name', max_length=50)
    kana = models.CharField(_('kana'), db_column='kana', db_index=True, max_length=100, null=True, blank=True)
    short_name = models.CharField(_('short_name'), db_column='short_name', max_length=50, null=True, blank=True)
    lat = models.FloatField(_('lat'), db_column='lat', db_index=True, default=0)
    lng = models.FloatField(_('lng'), db_column='lng', db_index=True, default=0)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'landmark'
        ordering = ['landmark_type_id', 'priority', 'kana', 'id']
        verbose_name = _('landmark')
        verbose_name_plural = _('landmarks')
