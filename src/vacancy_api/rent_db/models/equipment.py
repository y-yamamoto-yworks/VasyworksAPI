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
from .equipment_category import EquipmentCategory


class Equipment(models.Model):
    """
    設備
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=100)
    short_name = models.CharField(_('short_name'), db_column='short_name', max_length=50)

    category = models.ForeignKey(
        EquipmentCategory,
        db_column='category_id',
        related_name='category_elements',
        db_index=True,
        on_delete=models.PROTECT,
    )
    
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'equipment'
        ordering = ['priority', 'id']
        verbose_name = _('equipment')
        verbose_name_plural = _('equipments')

