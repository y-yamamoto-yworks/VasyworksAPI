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


class CleaningType(models.Model):
    """
    退去時清掃種別
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_paid = models.BooleanField(_('is_paid'), db_column='is_paid', default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cleaning_type'
        ordering = ['priority', 'id']
        verbose_name = _('cleaning_type')
        verbose_name_plural = _('cleaning_types')

    @property
    def is_money(self):
        if self.id in (2, 3, 4, 5):
            return True
        else:
            return False

