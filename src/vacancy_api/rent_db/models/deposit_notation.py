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


class DepositNotation(models.Model):
    """
    保証金表記
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    unit = models.CharField(_('unit'), db_column='unit', max_length=50, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'deposit_notation'
        ordering = ['priority', 'id']
        verbose_name = _('deposit_notation')
        verbose_name_plural = _('deposit_notations')

    @property
    def is_money(self):
        if self.id == 2:
            return True
        else:
            return False

    @property
    def is_month(self):
        if self.id == 3:
            return True
        else:
            return False

    @property
    def is_rate(self):
        if self.id == 4:
            return True
        else:
            return False
