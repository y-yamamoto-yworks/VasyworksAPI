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


class MonthDay(models.Model):
    """
    月間日付
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    from_day = models.IntegerField(_('from_day'), db_column='from_day', db_index=True, default=0)
    to_day = models.IntegerField(_('to_day'), db_column='to_day', db_index=True, default=0)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'month_day'
        ordering = ['priority', 'id']
        verbose_name = _('month_day')
        verbose_name_plural = _('month_days')

