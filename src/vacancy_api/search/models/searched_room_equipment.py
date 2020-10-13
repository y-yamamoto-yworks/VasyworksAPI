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
from rent_db.models import *


class SearchedRoomEquipment(models.Model):
    """部屋設備"""
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    room_oid = models.CharField(_('room_oid'), db_column='room_oid', db_index=True, unique=True, max_length=50)
    equipment_id = models.IntegerField(_('equipment_id'), db_column='equipment_id', db_index=True, default=0)
    name = models.CharField(_('name'), db_column='name', max_length=100)
    short_name = models.CharField(_('short_name'), db_column='short_name', max_length=50)


    class Meta:
        managed = False

    """
    検索関連
    """
    @classmethod
    def get_equipments(cls, room_id: int):
        """部屋の取得"""
        params = {}

        sql = 'SELECT {0} FROM {1} WHERE {2} ORDER BY {3};'.format(
            cls.get_sql_columns(),
            cls.get_sql_tables(room_id=room_id, params=params),
            cls.get_sql_conditions(params=params),
            cls.get_sql_orders(params=params),
        )

        ans = cls.objects.raw(raw_query=sql, params=params)

        return ans

    @classmethod
    def get_sql_columns(cls):
        """SQLのカラム一覧"""
        ans = 'room_equipment.id'
        ans += ', room.oid AS room_oid'
        ans += ', room_equipment.equipment_id'
        ans += ', equipment.name'
        ans += ', equipment.short_name'

        return ans

    @classmethod
    def get_sql_tables(cls, room_id: int, params):
        """SQLのテーブル一覧"""
        ans = 'room_equipment'
        ans += ' INNER JOIN room ON room_equipment.room_id = room.id'
        ans += ' AND room_equipment.room_id = %(room_id)s'
        ans += ' INNER JOIN equipment ON room_equipment.equipment_id = equipment.id'
        ans += ' INNER JOIN equipment_category ON equipment.category_id = equipment_category.id'

        params['room_id'] = room_id

        return ans

    @classmethod
    def get_sql_conditions(cls, params):
        """SQLの条件一覧"""
        ans = 'room_equipment.is_deleted = FALSE'
        ans += ' AND equipment.is_stopped = FALSE'

        target_equipments = (
            101010,         # システムキッチン
            102040,         # 追い焚き風呂
            103010,         # 独立洗面台
            103011,         # シャンプードレッサー
            104010,         # 温水洗浄便座
            105010,         # エアコン
            107100,         # TV付インターフォン
            109020,         # ウォークインクローゼット
            110010,         # ロフト
            111010,         # リノベーション
            111020,         # バリアフリー
            113010,         # オートロック
            114020,         # DIY可
            201010,         # エレベータ
            201020,         # 宅配ボックス
            201100,         # 24時間ゴミ出し
            202010,         # デザイナーズマンション
            301010,         # 居抜き店舗
            301020,         # スケルトン
            301030,         # 1階店舗
            301040,         # 飲食可
            301050,         # 事務所向け
            301060,         # SOHO
            301070,         # 住宅付店舗
        )
        ans += ' AND room_equipment.equipment_id IN ({0})'.format(','.join(map(str, target_equipments)))

        return ans

    @classmethod
    def get_sql_orders(cls, params):
        """SQLの並び順一覧"""
        ans = 'room_equipment.priority, equipment_category.priority, equipment.priority, room_equipment.id'
        return ans
