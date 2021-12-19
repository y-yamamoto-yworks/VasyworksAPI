"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lib.convert import *
from lib.functions import *
from .landmark import Landmark


class BuildingLandmark(models.Model):
    """
    建物ランドマーク
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    building = models.ForeignKey(
        'Building',
        db_column='building_id',
        related_name='building_landmarks',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )

    landmark = models.ForeignKey(
        Landmark,
        db_column='landmark_id',
        related_name='building_landmarks',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    distance = models.IntegerField(_('distance'), db_column='distance', default=0)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)

    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'building_landmark'
        ordering = ['priority', 'id']
        verbose_name = _('building_landmark')
        verbose_name_plural = _('building_landmarks')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)

    @property
    def building_oid(self):
        return self.building.oid

    @property
    def distance_text(self):
        """距離"""
        ans = None
        if self.distance > 0:
            ans = '{0}m'.format(self.distance)

        return ans
