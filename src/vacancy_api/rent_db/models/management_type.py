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


class ManagementType(models.Model):
    """
    管理種別
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_own = models.BooleanField(_('is_own'), db_column='is_own', default=False)
    is_entrusted = models.BooleanField(_('is_entrusted'), db_column='is_entrusted', default=False)
    is_condo_management = models.BooleanField(_('is_condo_management'), db_column='is_condo_management', default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'management_type'
        ordering = ['priority', 'id']
        verbose_name = _('management_type')
        verbose_name_plural = _('management_types')
