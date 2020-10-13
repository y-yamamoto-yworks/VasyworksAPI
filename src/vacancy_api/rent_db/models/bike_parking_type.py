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


class BikeParkingType(models.Model):
    """
    駐輪場種別
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_exist = models.BooleanField(_('is_exist'), db_column='is_exist', default=False)
    is_paid = models.BooleanField(_('is_paid'), db_column='is_paid', default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bike_parking_type'
        ordering = ['priority', 'id']
        verbose_name = _('bike_parking_type')
        verbose_name_plural = _('bike_parking_types')

