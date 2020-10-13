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


class CondoFeesType(models.Model):
    """
    共益費種別
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'condo_fees_type'
        ordering = ['priority', 'id']
        verbose_name = _('condo_fees_type')
        verbose_name_plural = _('condo_fees_types')

    @property
    def is_money(self):
        if self.id == 10:
            return True
        else:
            return False

