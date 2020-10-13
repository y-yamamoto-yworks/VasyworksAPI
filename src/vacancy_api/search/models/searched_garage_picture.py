"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.conf import settings
from django.db import models
from django.db.models import Q, Subquery, OuterRef
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lib.convert import *
from lib.functions import *
from lib.cache_file_helper import CacheFileHelper
from rent_db.models import *


class SearchedGaragePicture(models.Model):
    """駐車場写真（建物駐車場写真）"""
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    building_oid = models.CharField(_('building_oid'), db_column='building_oid', db_index=True, unique=True, max_length=50)
    file_oid = models.CharField(_('file_oid'), db_column='file_oid', db_index=True, unique=True, max_length=50)
    file_name = models.CharField(_('file_name'), db_column='file_name', max_length=255)
    cache_name_thumb = models.CharField(_('cache_name_thumb'), db_column='cache_name_thumb', max_length=255)
    cache_name_s = models.CharField(_('cache_name_s'), db_column='cache_name_s', max_length=255)
    cache_name_m = models.CharField(_('cache_name_m'), db_column='cache_name_m', max_length=255)
    cache_name_l = models.CharField(_('cache_name_l'), db_column='cache_name_l', max_length=255)
    comment = models.CharField(_('comment'), db_column='comment', max_length=50, null=True, blank=True)

    class Meta:
        managed = False

    """
    検索関連
    """
    @classmethod
    def get_picture(cls, building_id: int):
        """建物外観写真の取得"""
        params = {}

        sql = 'SELECT {0} FROM {1} WHERE {2} ORDER BY {3} LIMIT 1;'.format(
            cls.get_sql_columns(),
            cls.get_sql_tables(building_id=building_id, params=params),
            cls.get_sql_conditions(params=params),
            cls.get_sql_orders(params=params),
        )

        ans = None
        try:
            ans = cls.objects.raw(raw_query=sql, params=params)[0]
        except IndexError:
            ans = None

        return ans

    @classmethod
    def get_sql_columns(cls):
        """SQLのカラム一覧"""
        ans = 'building_picture.id'
        ans += ', building.oid AS building_oid'
        ans += ', building.file_oid AS file_oid'
        ans += ', building_picture.file_name'
        ans += ', building_picture.cache_name_thumb'
        ans += ', building_picture.cache_name_s'
        ans += ', building_picture.cache_name_m'
        ans += ', building_picture.cache_name_l'
        ans += ', building_picture.picture_type_id'
        ans += ', building_picture.comment'

        return ans

    @classmethod
    def get_sql_tables(cls, building_id: int, params):
        """SQLのテーブル一覧"""
        ans = 'building_picture'
        ans += ' INNER JOIN building ON building_picture.building_id = building.id AND building_picture.building_id = %(building_id)s'
        ans += ' AND building_picture.picture_type_id = 1040'       # 画像タイプが駐車場

        params['building_id'] = building_id

        return ans

    @classmethod
    def get_sql_conditions(cls, params):
        """SQLの条件一覧"""
        ans = 'building_picture.is_deleted = FALSE'
        ans += ' AND building_picture.is_publish_web = TRUE'

        return ans

    @classmethod
    def get_sql_orders(cls, params):
        """SQLの並び順一覧"""
        ans = 'building_picture.priority, building_picture.id'
        return ans

    """
    表示用プロパティ
    """
    @property
    def thumbnail_file_url(self):
        """サムネイルファイルのURLの取得"""
        return CacheFileHelper.get_property_image_file_url(
            self.file_oid,
            self.file_name,
            self.cache_name_thumb,
            Company.get_instance().water_mark,
            settings.THUMBNAIL_IMAGE_SIZE
        )

    @property
    def small_file_url(self):
        """小キャッシュファイルのURLの取得"""
        url = CacheFileHelper.get_property_image_file_url(
            self.file_oid,
            self.file_name,
            self.cache_name_s,
            Company.get_instance().water_mark,
            settings.SMALL_IMAGE_SIZE
        )

        return url

    @property
    def medium_file_url(self):
        """中キャッシュファイルのURLの取得"""
        url = CacheFileHelper.get_property_image_file_url(
            self.file_oid,
            self.file_name,
            self.cache_name_m,
            Company.get_instance().water_mark,
            settings.MEDIUM_IMAGE_SIZE
        )

        return url

    @property
    def large_file_url(self):
        """大キャッシュファイルのURLの取得"""
        url = CacheFileHelper.get_property_image_file_url(
            self.file_oid,
            self.file_name,
            self.cache_name_l,
            Company.get_instance().water_mark,
            settings.LARGE_IMAGE_SIZE
        )

        return url
