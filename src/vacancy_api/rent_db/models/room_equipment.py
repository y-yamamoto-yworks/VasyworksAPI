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
from .equipment import Equipment


class  RoomEquipment(models.Model):
    """
    部屋設備
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    building = models.ForeignKey(
        'Building',
        db_column='building_id',
        related_name='room_equipments',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    room = models.ForeignKey(
        'Room',
        db_column='room_id',
        related_name='room_equipments',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )

    equipment = models.ForeignKey(
        Equipment,
        db_column='equipment_id',
        related_name='room_equipments',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    is_remained = models.BooleanField(_('is_remained'), db_column='is_remained', default=False)
    note = models.TextField(_('note'), db_column='note', max_length=2000, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)

    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'room_equipment'
        ordering = ['priority', 'id']
        verbose_name = _('room_equipment')
        verbose_name_plural = _('room_equipments')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)

    @property
    def building_oid(self):
        return self.building.oid

    @property
    def room_oid(self):
        return self.room.oid
