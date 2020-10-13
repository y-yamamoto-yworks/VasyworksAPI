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
from .search_conditions import SearchConditions
from .searched_building_room import SearchedBuildingRoom
from .searched_building_exterior_picture import SearchedBuildingExteriorPicture


class SearchedBuilding(models.Model):
    """建物リスト"""
    conditions = None
    is_residential = True

    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    oid = models.CharField(_('oid'), db_column='oid', db_index=True, unique=True, max_length=50)
    building_code = models.CharField(_('building_code'), db_column='building_code', max_length=20, db_index=True, null=True, blank=True)
    building_name = models.CharField(_('building_name'), db_column='building_name', max_length=100, db_index=True, null=True, blank=True)
    building_kana = models.CharField(_('building_kana'), db_column='building_kana', max_length=100, db_index=True, null=True, blank=True)
    building_old_name = models.CharField(_('building_old_name'), db_column='building_old_name', max_length=100, null=True, blank=True)

    postal_code = models.CharField(_('postal_code'), db_column='postal_code', max_length=10, null=True, blank=True)
    pref = models.ForeignKey(
        Pref,
        db_column='pref_id',
        related_name='searched_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading_area=True) | Q(pk=0),
    )
    city = models.ForeignKey(
        City,
        db_column='city_id',
        related_name='searched_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading_area=True, is_stopped=False) | Q(pk=0),
    )
    town_address = models.CharField(_('town_address'), db_column='town_address', max_length=255, null=True, blank=True)
    town_name = models.CharField(_('town_name'), db_column='town_name', max_length=100, null=True, blank=True)
    house_no = models.CharField(_('house_no'), db_column='house_no', max_length=100, null=True, blank=True)
    building_no = models.CharField(_('building_no'), db_column='building_no', max_length=100, null=True, blank=True)
    lat = models.FloatField(_('lat'), db_column='lat', db_index=True, default=0)
    lng = models.FloatField(_('lng'), db_column='lng', db_index=True, default=0)
    area = models.ForeignKey(
        Area,
        db_column='area_id',
        related_name='searched_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False) | Q(pk=0),
    )
    department = models.ForeignKey(
        Department,
        db_column='department_id',
        related_name='searched_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    priority_level = models.IntegerField(_('priority_level'), db_column='priority_level', db_index=True, default=50)
    agency_department = models.ForeignKey(
        Department,
        db_column='agency_department_id',
        related_name='agency_searched_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    arrival_type1 = models.ForeignKey(
        ArrivalType,
        db_column='arrival_type_id1',
        related_name='searched_buildings1',
        on_delete=models.PROTECT,
        default=0,
    )
    station1 = models.ForeignKey(
        Station,
        db_column='station_id1',
        related_name='searched_buildings1',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading=True, is_stopped=False) | Q(pk=0),
    )
    station_time1 = models.IntegerField(_('station_time1'), db_column='station_time1', default=0)
    bus_stop1 = models.CharField(_('bus_stop1'), db_column='bus_stop1', max_length=50, null=True, blank=True)
    bus_stop_time1 = models.IntegerField(_('bus_stop_time1'), db_column='bus_stop_time1', default=0)

    arrival_type2 = models.ForeignKey(
        ArrivalType,
        db_column='arrival_type_id2',
        related_name='searched_buildings2',
        on_delete=models.PROTECT,
        default=0,
    )
    station2 = models.ForeignKey(
        Station,
        db_column='station_id2',
        related_name='searched_buildings2',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading=True, is_stopped=False) | Q(pk=0),
    )
    station_time2 = models.IntegerField(_('station_time2'), db_column='station_time2', default=0)
    bus_stop2 = models.CharField(_('bus_stop2'), db_column='bus_stop2', max_length=50, null=True, blank=True)
    bus_stop_time2 = models.IntegerField(_('bus_stop_time2'), db_column='bus_stop_time2', default=0)

    arrival_type3 = models.ForeignKey(
        ArrivalType,
        db_column='arrival_type_id3',
        related_name='searched_buildings3',
        on_delete=models.PROTECT,
        default=0,
    )
    station3 = models.ForeignKey(
        Station,
        db_column='station_id3',
        related_name='searched_buildings3',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading=True, is_stopped=False) | Q(pk=0),
    )
    station_time3 = models.IntegerField(_('station_time3'), db_column='station_time3', default=0)
    bus_stop3 = models.CharField(_('bus_stop3'), db_column='bus_stop3', max_length=50, null=True, blank=True)
    bus_stop_time3 = models.IntegerField(_('bus_stop_time3'), db_column='bus_stop_time3', default=0)

    building_type = models.ForeignKey(
        BuildingType,
        db_column='building_type_id',
        related_name='searched_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    structure = models.ForeignKey(
        Structure,
        db_column='structure_id',
        related_name='searched_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    building_rooms = models.IntegerField(_('building_rooms'), db_column='building_rooms', default=0)
    building_floors = models.IntegerField(_('building_floors'), db_column='building_floors', default=0)
    building_undergrounds = models.IntegerField(_('building_undergrounds'), db_column='building_undergrounds', default=0)
    build_year = models.IntegerField(_('build_year'), db_column='build_year', db_index=True, default=1970)
    build_month = models.IntegerField(_('build_month'), db_column='build_month', default=1)
    bike_parking_type = models.ForeignKey(
        BikeParkingType,
        db_column='bike_parking_type_id',
        related_name='searched_buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_type = models.ForeignKey(
        GarageType,
        db_column='garage_type_id',
        related_name='searched_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    web_catch_copy = models.CharField(_('web_catch_copy'), db_column='web_catch_copy', max_length=100, null=True, blank=True)
    web_appeal = models.CharField(_('web_appeal'), db_column='web_appeal', max_length=255, null=True, blank=True)

    class Meta:
        managed = False

    """
    検索関連
    """
    @classmethod
    def get_buildings(cls, conditions: SearchConditions, is_residential):
        """クエリセットの取得"""
        params = {}

        sql = 'SELECT {0} FROM {1} WHERE {2} ORDER BY {3};'.format(
            cls.__get_sql_columns(),
            cls.__get_sql_tables(conditions=conditions, params=params, is_residential=is_residential),
            cls.__get_sql_conditions(conditions=conditions, params=params),
            cls.__get_sql_orders(conditions=conditions, params=params),
        )

        ans = cls.objects.raw(raw_query=sql, params=params)

        return ans

    """
    SQL関連内部メソッド
    """
    @classmethod
    def __get_sql_columns(cls):
        """SQLのカラム一覧"""
        ans = 'building.id'
        ans += ', building.oid'
        ans += ', building.building_code'
        ans += ', building.building_name'
        ans += ', building.building_kana'
        ans += ', building.building_old_name'
        ans += ', building.postal_code'
        ans += ', building.pref_id'
        ans += ', building.city_id'
        ans += ', building.town_address'
        ans += ', building.town_name'
        ans += ', building.house_no'
        ans += ', building.building_no'
        ans += ', building.lat'
        ans += ', building.lng'
        ans += ', building.area_id'
        ans += ', building.department_id'
        ans += ', building.agency_department_id'
        ans += ', building.arrival_type_id1'
        ans += ', building.station_id1'
        ans += ', building.station_time1'
        ans += ', building.bus_stop1'
        ans += ', building.bus_stop_time1'
        ans += ', building.arrival_type_id2'
        ans += ', building.station_id2'
        ans += ', building.station_time2'
        ans += ', building.bus_stop2'
        ans += ', building.bus_stop_time2'
        ans += ', building.arrival_type_id3'
        ans += ', building.station_id3'
        ans += ', building.station_time3'
        ans += ', building.bus_stop3'
        ans += ', building.bus_stop_time3'
        ans += ', building.building_type_id'
        ans += ', building.structure_id'
        ans += ', building.building_rooms'
        ans += ', building.building_floors'
        ans += ', building.building_undergrounds'
        ans += ', building.build_year'
        ans += ', building.build_month'
        ans += ', building.bike_parking_type_id'
        ans += ', building.garage_type_id'
        ans += ', building.web_catch_copy'
        ans += ', building.web_appeal'

        return ans

    @classmethod
    def __get_sql_tables(cls, conditions: SearchConditions, params, is_residential):
        """SQLのテーブル一覧"""
        ans = 'building'
        ans += ' INNER JOIN building_type ON building.building_type_id = building_type.id'
        if is_residential:
            ans += ' AND building_type.is_residential = TRUE'
        else:
            ans += ' AND building_type.is_building = TRUE'
        ans += ' INNER JOIN garage_type ON building.garage_type_id = garage_type.id'
        ans += ' INNER JOIN bike_parking_type ON building.bike_parking_type_id = bike_parking_type.id'
        ans += ' INNER JOIN pref ON building.pref_id = pref.id'
        ans += ' INNER JOIN city ON building.city_id = city.id'

        if conditions:
            # 管理種別の限定有無
            ans += xstr(conditions.get_no_limit_sql(is_building=True))

            # ランドマーク
            ans += xstr(conditions.get_landmarks_sql(params=params))

            # 設備条件
            ans += xstr(conditions.get_only_top_floor_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_system_kitchen_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_washstand_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_aircon_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_auto_lock_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_designers_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_elevator_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_delivery_box_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_reheating_bath_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_washing_toilet_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_tv_intercom_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_loft_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_renovation_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_diy_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_walk_in_closet_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_barrier_free_sql(is_building=True, is_residential=is_residential))
            ans += xstr(conditions.get_garbage_box_24_sql(is_building=True, is_residential=is_residential))
            if not is_residential:
                ans += xstr(conditions.get_tenant_furnished_shop_sql(is_building=True))
                ans += xstr(conditions.get_tenant_skeleton_sql(is_building=True))
                ans += xstr(conditions.get_tenant_restaurant_sql(is_building=True))
                ans += xstr(conditions.get_tenant_office_sql(is_building=True))
                ans += xstr(conditions.get_tenant_first_floor_sql(is_building=True))
                ans += xstr(conditions.get_tenant_soho_sql(is_building=True))
                ans += xstr(conditions.get_tenant_residence_sql(is_building=True))

        # 部屋抽出条件
        ans += ' INNER JOIN ('

        ans += 'SELECT room.building_id FROM {0} WHERE {1} GROUP BY room.building_id'.format(
            cls.__get_sql_room_tables(conditions=conditions, params=params, is_residential=is_residential),
            cls.__get_sql_room_conditions(conditions=conditions, params=params),
        )
        ans += ') room_matching ON building.id = room_matching.building_id'

        # 並び順処理用
        if conditions:
            ans += xstr(conditions.get_building_room_sql(is_residential=is_residential))
            ans += xstr(conditions.get_new_arrival_sql(is_building=True, is_residential=is_residential))

        return ans

    @classmethod
    def __get_sql_room_tables(cls, conditions: SearchConditions, params, is_residential):
        """SQLの部屋テーブル一覧"""
        ans = 'room'
        ans += ' INNER JOIN building ON room.building_id = building.id'
        ans += ' INNER JOIN room_status ON room.room_status_id = room_status.id AND room_status.for_rent = TRUE'
        ans += ' INNER JOIN rental_type ON room.rental_type_id = rental_type.id'
        if is_residential:
            ans += ' AND rental_type.is_residential = TRUE'
        else:
            ans += ' AND rental_type.is_non_residential = TRUE'
        ans += ' INNER JOIN pet_type on room.pet_type_id = pet_type.id'

        if conditions:
            # 管理種別の限定有無
            ans += xstr(conditions.get_no_limit_sql(is_building=False))

        return ans

    @classmethod
    def __get_sql_conditions(cls, conditions: SearchConditions, params):
        """SQLの建物用条件一覧"""
        ans = 'building.is_deleted = FALSE'
        ans += ' AND building.is_hidden_web = FALSE'

        if conditions:
            ans += cls.__and_condition_sql(conditions.get_stations_sql(params=params), ans)
            ans += cls.__and_condition_sql(conditions.get_cities_sql(params=params), ans)
            ans += cls.__and_condition_sql(conditions.get_areas_sql(params=params), ans)
            ans += cls.__and_condition_sql(conditions.get_latlng_sql(params=params), ans)
            ans += cls.__and_condition_sql(conditions.get_elementary_school_sql(params=params), ans)
            ans += cls.__and_condition_sql(conditions.get_building_types_sql(params=params), ans)
            ans += cls.__and_condition_sql(conditions.get_building_age_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_with_garage_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_with_bike_parking_sql(), ans)

        return ans

    @classmethod
    def __get_sql_room_conditions(cls, conditions: SearchConditions, params):
        """SQLの部屋用条件一覧"""
        ans = 'room.is_deleted = FALSE AND room.is_publish_web = TRUE'
        ans += ' AND building.is_deleted = FALSE AND building.is_hidden_web = FALSE'

        if conditions:
            ans += cls.__and_condition_sql(conditions.get_rent_sql(params=params), ans)
            ans += cls.__and_condition_sql(conditions.get_free_rent_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_without_deposit_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_layout_types_sql(params=params), ans)
            ans += cls.__and_condition_sql(conditions.get_only_first_floor_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_over_second_floor_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_directions_sql(params=params), ans)
            ans += cls.__and_condition_sql(conditions.get_gas_kitchen_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_separate_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_free_internet_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_indoor_washer_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_pet_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_instrument_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_live_together_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_children_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_room_share_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_non_japanese_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_new_student_sql(), ans)
            ans += cls.__and_condition_sql(conditions.get_office_use_sql(), ans)

        return ans

    @classmethod
    def __and_condition_sql(cls, condition_sql, sql):
        """SQL文字列に条件SQLをAND条件で追加"""
        ans = ''
        if xstr(condition_sql):
            if xstr(sql) != '':
                ans += " AND "
            ans += xstr(condition_sql)
        return ans


    @classmethod
    def __get_sql_orders(cls, conditions: SearchConditions, params):
        """SQLの並び順一覧"""
        ans = ''

        if conditions:
            ans += xstr(conditions.get_order_by_sql())

        if ans != '':
            ans += ", "
        ans += 'building.priority_level DESC'
        ans += ', pref.priority, city.priority, building.building_kana'

        return ans

    """
    プロパティ
    """
    @property
    def rooms(self):
        return SearchedBuildingRoom.get_rooms(
            building_id=self.id,
            conditions=self.conditions,
            is_residential=self.is_residential,
        )

    @property
    def exterior_picture(self):
        return SearchedBuildingExteriorPicture.get_picture(self.id)

    """
    表示用プロパティ
    """
    @property
    def address(self):
        return DataHelper.get_address_text(
            self.pref,
            self.city,
            self.town_address,
            self.house_no,
            self.building_no)

    @property
    def area_text(self):
        return DataHelper.get_area_text(self.area)

    @property
    def nearest_station1(self):
        return DataHelper.get_nearest_station_text(
            self.arrival_type1,
            self.station1,
            self.station_time1,
            self.bus_stop1,
            self.bus_stop_time1)

    @property
    def nearest_station2(self):
        return DataHelper.get_nearest_station_text(
            self.arrival_type2,
            self.station2,
            self.station_time2,
            self.bus_stop2,
            self.bus_stop_time2)

    @property
    def nearest_station3(self):
        return DataHelper.get_nearest_station_text(
            self.arrival_type3,
            self.station3,
            self.station_time3,
            self.bus_stop3,
            self.bus_stop_time3)

    @property
    def building_type_text(self):
        return DataHelper.get_building_type_text(
            self.building_type)

    @property
    def build_year_month(self):
        return DataHelper.get_build_year_month_text(
            self.build_year,
            self.build_month)

    @property
    def structure_text(self):
        return DataHelper.get_structure_text(
            self.structure)

    @property
    def garage_type_text(self):
        return DataHelper.get_garage_type_text(self.garage_type)

    @property
    def bike_parking_type_text(self):
        return DataHelper.get_bike_parking_type_text(self.bike_parking_type)
