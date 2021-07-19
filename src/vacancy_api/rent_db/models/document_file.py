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
from lib.cache_file_helper import CacheFileHelper


class DocumentFile(models.Model):
    """
    書類ファイル
    """
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    file_name = models.CharField(_('file_name'), db_column='file_name', max_length=255)
    cache_name = models.CharField(_('cache_name'), db_column='cache_name', max_length=255)
    file_title = models.CharField(_('file_title'), db_column='file_title', max_length=255, null=True, blank=True)
    is_publish_web = models.BooleanField(_('is_publish_web'), db_column='is_publish_web', db_index=True, default=False)
    is_publish_vacancy = models.BooleanField(_('is_publish_vacancy'), db_column='is_publish_vacancy', db_index=True, default=True)
    comment = models.CharField(_('comment'), db_column='comment', max_length=50, null=True, blank=True)
    note = models.CharField(_('note'), db_column='note', max_length=255, null=True, blank=True)
    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)

    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    def __str__(self):
        return self.file_name

    class Meta:
        managed = False
        db_table = 'document_file'
        ordering = ['priority', 'id']
        verbose_name = _('document_file')
        verbose_name_plural = _('document_files')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)

    @property
    def file_url(self):
        """キャッシュファイルのURLの取得"""
        url = CacheFileHelper.get_document_file_url(
            self.file_name,
            self.cache_name,
        )

        return url
