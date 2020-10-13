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
from .staff import Staff


class Department(models.Model):
    """
    部署
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    department_name = models.CharField(_('department_name'), db_column='department_name', max_length=100, db_index=True, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    postal_code = models.CharField(_('postal_code'), db_column='postal_code', max_length=10, null=True, blank=True)
    address = models.CharField(_('address'), db_column='address', max_length=255, null=True, blank=True)
    tel = models.CharField(_('tel'), db_column='tel', max_length=20, null=True, blank=True)
    fax = models.CharField(_('fax'), db_column='fax', max_length=20, null=True, blank=True)
    mail = models.EmailField(_('mail'), db_column='mail', null=True, blank=True)
    is_publish_vacancy = models.BooleanField(_('is_publish_vacancy'), db_column='is_publish_vacancy', db_index=True, default=True)
    note = models.TextField(_('note'), db_column='note', max_length=2000, null=True, blank=True)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)
    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.department_name

    class Meta:
        managed = False
        db_table = 'department'
        ordering = ['priority', 'id']
        verbose_name = _('department')
        verbose_name_plural = _('departments')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)

    @property
    def publish_staffs(self):
        return self.staffs.filter(
            is_publish_vacancy=True,
            is_stopped=False,
            is_deleted=False,
        ).order_by('priority', 'id').all()
