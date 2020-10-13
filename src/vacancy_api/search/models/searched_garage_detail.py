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
from lib.data_helper import DataHelper
from rent_db.models import *


class SearchedGarageDetail(models.Model):
    """駐車場詳細リスト（建物駐車場リスト）"""
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    building_oid = models.CharField(_('building_oid'), db_column='building_oid', db_index=True, unique=True, max_length=50)
    garage_name = models.CharField(_('garage_name'), db_column='garage_name', max_length=100)
    garage_fee = models.IntegerField(_('garage_fee'), db_column='garage_fee', default=0)
    garage_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='garage_fee_tax_type_id',
        related_name='searched_garage_fees',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_charge = models.IntegerField(_('garage_charge'), db_column='garage_charge', default=0)
    garage_charge_tax_type = models.ForeignKey(
        TaxType,
        db_column='garage_charge_tax_type_id',
        related_name='searched_garage_charges',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_deposit = models.IntegerField(_('garage_deposit'), db_column='garage_deposit', default=0)
    garage_deposit_tax_type = models.ForeignKey(
        TaxType,
        db_column='garage_deposit_tax_type_id',
        related_name='searched_garage_deposits',
        on_delete=models.PROTECT,
        default=0,
    )
    certification_fee = models.IntegerField(_('certification_fee'), db_column='certification_fee', default=0)
    certification_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='certification_fee_tax_type_id',
        related_name='searched_certification_fees',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name1 = models.CharField(_('initial_cost_name1'), db_column='initial_cost_name1', max_length=100, null=True, blank=True)
    initial_cost1 = models.IntegerField(_('initial_cost1'), db_column='initial_cost1', default=0)
    initial_cost_tax_type1 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id1',
        related_name='searched_initial_costs1',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name2 = models.CharField(_('initial_cost_name2'), db_column='initial_cost_name2', max_length=100, null=True, blank=True)
    initial_cost2 = models.IntegerField(_('initial_cost2'), db_column='initial_cost2', default=0)
    initial_cost_tax_type2 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id2',
        related_name='searched_initial_costs2',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name3 = models.CharField(_('initial_cost_name3'), db_column='initial_cost_name3', max_length=100, null=True, blank=True)
    initial_cost3 = models.IntegerField(_('initial_cost3'), db_column='initial_cost3', default=0)
    initial_cost_tax_type3 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id3',
        related_name='searched_initial_costs3',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_status = models.ForeignKey(
        GarageStatus,
        db_column='garage_status_id',
        related_name='searched_building_garages',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    width = models.DecimalField(_('width'), db_column='width', default=0, max_digits=12, decimal_places=2)
    length = models.DecimalField(_('length'), db_column='length', default=0, max_digits=12, decimal_places=2)
    height = models.DecimalField(_('height'), db_column='height', default=0, max_digits=12, decimal_places=2)
    comment = models.CharField(_('comment'), db_column='comment', max_length=100, null=True, blank=True)

    class Meta:
        managed = False

    """
    検索関連
    """
    @classmethod
    def get_garage_details(cls, building_id: int):
        """駐車場詳細（建物駐車場）の取得"""
        params = {}

        sql = 'SELECT {0} FROM {1} WHERE {2} ORDER BY {3};'.format(
            cls.__get_sql_columns(),
            cls.__get_sql_tables(building_id=building_id, params=params),
            cls.__get_sql_conditions(),
            cls.__get_sql_orders(),
        )

        ans = cls.objects.raw(raw_query=sql, params=params)

        return ans

    """
    SQL関連内部メソッド
    """
    @classmethod
    def __get_sql_columns(cls):
        """SQLのカラム一覧"""
        ans = 'building_garage.id'
        ans += ', building.oid AS building_oid'
        ans += ', building_garage.garage_name'
        ans += ', building_garage.garage_fee'
        ans += ', building_garage.garage_fee_tax_type_id'
        ans += ', building_garage.garage_charge'
        ans += ', building_garage.garage_charge_tax_type_id'
        ans += ', building_garage.garage_deposit'
        ans += ', building_garage.garage_deposit_tax_type_id'
        ans += ', building_garage.certification_fee'
        ans += ', building_garage.certification_fee_tax_type_id'
        ans += ', building_garage.initial_cost_name1'
        ans += ', building_garage.initial_cost1'
        ans += ', building_garage.initial_cost_tax_type_id1'
        ans += ', building_garage.initial_cost_name2'
        ans += ', building_garage.initial_cost2'
        ans += ', building_garage.initial_cost_tax_type_id2'
        ans += ', building_garage.initial_cost_name3'
        ans += ', building_garage.initial_cost3'
        ans += ', building_garage.initial_cost_tax_type_id3'
        ans += ', building_garage.garage_status_id'
        ans += ', building_garage.width'
        ans += ', building_garage.length'
        ans += ', building_garage.height'
        ans += ', building_garage.comment'

        return ans

    @classmethod
    def __get_sql_tables(cls, building_id: int, params):
        """SQLのテーブル一覧"""
        ans = 'building_garage'
        ans += ' INNER JOIN building ON building_garage.building_id = building.id'
        ans += ' AND building_garage.building_id = %(building_id)s'
        params['building_id'] = building_id

        return ans

    @classmethod
    def __get_sql_conditions(cls):
        """SQLの条件一覧"""
        ans = 'building_garage.is_deleted = FALSE'
        ans += ' AND building_garage.allow_no_room = TRUE'      # 外部貸し可
        ans += ' AND building_garage.garage_status_id IN (1, 3, 4)'       # 空き有・要確認・別参照
        return ans

    @classmethod
    def __get_sql_orders(cls):
        """SQLの並び順一覧"""
        ans = 'building_garage.priority, building_garage.garage_name, building_garage.id'
        return ans

    """
    表示用プロパティ
    """
    @property
    def garage_status_text(self):
        return DataHelper.get_garage_status_text(self.garage_status)

    @property
    def garage_fee_text(self):
        return DataHelper.get_cost_text(
            '駐車場月額',        # dummy
            self.garage_fee,
            self.garage_fee_tax_type)

    @property
    def garage_charge_text(self):
        return DataHelper.get_cost_text(
            '駐車場手数料',       # dummy
            self.garage_charge,
            self.garage_charge_tax_type)

    @property
    def garage_deposit_text(self):
        return DataHelper.get_cost_text(
            '駐車場保証料',       # dummy
            self.garage_deposit,
            self.garage_deposit_tax_type)

    @property
    def certification_fee_text(self):
        return DataHelper.get_cost_text(
            '車庫証明手数料',       # dummy
            self.certification_fee,
            self.certification_fee_tax_type)

    @property
    def initial_cost_text1(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name1,
            self.initial_cost1,
            self.initial_cost_tax_type1)

    @property
    def initial_cost_text2(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name2,
            self.initial_cost2,
            self.initial_cost_tax_type2)

    @property
    def initial_cost_text3(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name3,
            self.initial_cost3,
            self.initial_cost_tax_type3)

    @property
    def garage_size_text(self):
        return DataHelper.get_garage_size_text(
            self.width,
            self.length,
            self.height)
