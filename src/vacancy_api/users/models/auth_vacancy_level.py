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


class VacancyLevel(models.Model):
    """
    空室情報ユーザ閲覧レベル
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    level = models.IntegerField(_('level'), db_column='level', db_index=True, default=0)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'auth_vacancy_level'
        ordering = ['priority', 'id']
        verbose_name = _('vacancy_level')
        verbose_name_plural = _('vacancy_levels')

