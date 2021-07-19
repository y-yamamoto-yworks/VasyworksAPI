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


class TaxType(models.Model):
    """
    税種別
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tax_type'
        ordering = ['priority', 'id']
        verbose_name = _('tax_type')
        verbose_name_plural = _('tax_types')

    @property
    def is_excluding(self):
        """税別"""
        if self.id == 1:
            return True
        else:
            return False

    @property
    def is_including(self):
        """税込"""
        if self.id == 2:
            return True
        else:
            return False

    @property
    def text(self):
        ans = ''
        if self.is_excluding or self.is_including:
            ans = self.name

        return ans

