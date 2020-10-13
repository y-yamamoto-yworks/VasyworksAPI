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
from .searched_building_exterior_picture import SearchedBuildingExteriorPicture
from .searched_room_interior_picture import SearchedRoomInteriorPicture
from .searched_room_layout_picture import SearchedRoomLayoutPicture
from .searched_room_equipment import SearchedRoomEquipment


class SearchedRoom(models.Model):
    """部屋リスト"""
    id = models.AutoField(_('id'), db_column='id', primary_key=True)
    oid = models.CharField(_('oid'), db_column='oid', db_index=True, unique=True, max_length=50)
    building_id = models.IntegerField(_('building_id'), db_column='building_id', db_index=True, default=0)
    building_oid = models.CharField(_('building_oid'), db_column='building_oid', db_index=True, unique=True, max_length=50)
    building_code = models.CharField(_('building_code'), db_column='building_code', max_length=20, db_index=True, null=True, blank=True)
    building_name = models.CharField(_('building_name'), db_column='building_name', max_length=100, db_index=True, null=True, blank=True)
    building_kana = models.CharField(_('building_kana'), db_column='building_kana', max_length=100, db_index=True, null=True, blank=True)
    building_old_name = models.CharField(_('building_old_name'), db_column='building_old_name', max_length=100, null=True, blank=True)

    postal_code = models.CharField(_('postal_code'), db_column='postal_code', max_length=10, null=True, blank=True)
    pref = models.ForeignKey(
        Pref,
        db_column='pref_id',
        related_name='searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading_area=True) | Q(pk=0),
    )
    city = models.ForeignKey(
        City,
        db_column='city_id',
        related_name='searched_rooms',
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
        related_name='searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False) | Q(pk=0),
    )
    department = models.ForeignKey(
        Department,
        db_column='department_id',
        related_name='searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    priority_level = models.IntegerField(_('priority_level'), db_column='priority_level', db_index=True, default=50)
    agency_department = models.ForeignKey(
        Department,
        db_column='agency_department_id',
        related_name='agency_searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    arrival_type1 = models.ForeignKey(
        ArrivalType,
        db_column='arrival_type_id1',
        related_name='searched_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    station1 = models.ForeignKey(
        Station,
        db_column='station_id1',
        related_name='searched_rooms1',
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
        related_name='searched_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    station2 = models.ForeignKey(
        Station,
        db_column='station_id2',
        related_name='searched_rooms2',
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
        related_name='searched_rooms3',
        on_delete=models.PROTECT,
        default=0,
    )
    station3 = models.ForeignKey(
        Station,
        db_column='station_id3',
        related_name='searched_rooms3',
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
        related_name='searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    structure = models.ForeignKey(
        Structure,
        db_column='structure_id',
        related_name='searched_rooms',
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
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_type = models.ForeignKey(
        GarageType,
        db_column='garage_type_id',
        related_name='searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )

    room_no = models.CharField(_('room_no'), db_column='room_no', max_length=20, db_index=True, null=True, blank=True)
    room_floor = models.IntegerField(_('room_floor'), db_column='room_floor', default=0)

    rental_type = models.ForeignKey(
        RentalType,
        db_column='rental_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    room_status = models.ForeignKey(
        RoomStatus,
        db_column='room_status_id',
        related_name='searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    vacancy_status = models.ForeignKey(
        VacancyStatus,
        db_column='vacancy_status_id',
        related_name='searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    layout_type = models.ForeignKey(
        LayoutType,
        db_column='layout_type_id',
        related_name='searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    western_style_room1 = models.DecimalField(_('western_style_room1'), db_column='western_style_room1', default=0, max_digits=5, decimal_places=2)
    western_style_room2 = models.DecimalField(_('western_style_room2'), db_column='western_style_room2', default=0, max_digits=5, decimal_places=2)
    western_style_room3 = models.DecimalField(_('western_style_room3'), db_column='western_style_room3', default=0, max_digits=5, decimal_places=2)
    western_style_room4 = models.DecimalField(_('western_style_room4'), db_column='western_style_room4', default=0, max_digits=5, decimal_places=2)
    western_style_room5 = models.DecimalField(_('western_style_room5'), db_column='western_style_room5', default=0, max_digits=5, decimal_places=2)
    western_style_room6 = models.DecimalField(_('western_style_room6'), db_column='western_style_room6', default=0, max_digits=5, decimal_places=2)
    western_style_room7 = models.DecimalField(_('western_style_room7'), db_column='western_style_room7', default=0, max_digits=5, decimal_places=2)
    western_style_room8 = models.DecimalField(_('western_style_room8'), db_column='western_style_room8', default=0, max_digits=5, decimal_places=2)
    western_style_room9 = models.DecimalField(_('western_style_room9'), db_column='western_style_room9', default=0, max_digits=5, decimal_places=2)
    western_style_room10 = models.DecimalField(_('western_style_room10'), db_column='western_style_room10', default=0, max_digits=5, decimal_places=2)
    japanese_style_room1 = models.DecimalField(_('japanese_style_room1'), db_column='japanese_style_room1', default=0, max_digits=5, decimal_places=2)
    japanese_style_room2 = models.DecimalField(_('japanese_style_room2'), db_column='japanese_style_room2', default=0, max_digits=5, decimal_places=2)
    japanese_style_room3 = models.DecimalField(_('japanese_style_room3'), db_column='japanese_style_room3', default=0, max_digits=5, decimal_places=2)
    japanese_style_room4 = models.DecimalField(_('japanese_style_room4'), db_column='japanese_style_room4', default=0, max_digits=5, decimal_places=2)
    japanese_style_room5 = models.DecimalField(_('japanese_style_room5'), db_column='japanese_style_room5', default=0, max_digits=5, decimal_places=2)
    japanese_style_room6 = models.DecimalField(_('japanese_style_room6'), db_column='japanese_style_room6', default=0, max_digits=5, decimal_places=2)
    japanese_style_room7 = models.DecimalField(_('japanese_style_room7'), db_column='japanese_style_room7', default=0, max_digits=5, decimal_places=2)
    japanese_style_room8 = models.DecimalField(_('japanese_style_room8'), db_column='japanese_style_room8', default=0, max_digits=5, decimal_places=2)
    japanese_style_room9 = models.DecimalField(_('japanese_style_room9'), db_column='japanese_style_room9', default=0, max_digits=5, decimal_places=2)
    japanese_style_room10 = models.DecimalField(_('japanese_style_room10'), db_column='japanese_style_room10', default=0, max_digits=5, decimal_places=2)
    kitchen_type1 = models.ForeignKey(
        KitchenType,
        db_column='kitchen_type_id1',
        related_name='searched_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    kitchen1 = models.DecimalField(_('kitchen1'), db_column='kitchen1', default=0, max_digits=5, decimal_places=2)
    kitchen_type2 = models.ForeignKey(
        KitchenType,
        db_column='kitchen_type_id2',
        related_name='searched_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    kitchen2 = models.DecimalField(_('kitchen2'), db_column='kitchen2', default=0, max_digits=5, decimal_places=2)
    kitchen_type3 = models.ForeignKey(
        KitchenType,
        db_column='kitchen_type_id3',
        related_name='searched_rooms3',
        on_delete=models.PROTECT,
        default=0,
    )
    kitchen3 = models.DecimalField(_('kitchen3'), db_column='kitchen3', default=0, max_digits=5, decimal_places=2)
    store_room1 = models.DecimalField(_('store_room1'), db_column='store_room1', default=0, max_digits=5, decimal_places=2)
    store_room2 = models.DecimalField(_('store_room2'), db_column='store_room2', default=0, max_digits=5, decimal_places=2)
    store_room3 = models.DecimalField(_('store_room3'), db_column='store_room3', default=0, max_digits=5, decimal_places=2)
    loft1 = models.DecimalField(_('loft1'), db_column='loft1', default=0, max_digits=5, decimal_places=2)
    loft2 = models.DecimalField(_('loft2'), db_column='loft2', default=0, max_digits=5, decimal_places=2)
    sun_room1 = models.DecimalField(_('sun_room1'), db_column='sun_room1', default=0, max_digits=5, decimal_places=2)
    sun_room2 = models.DecimalField(_('sun_room2'), db_column='sun_room2', default=0, max_digits=5, decimal_places=2)
    layout_note = models.CharField(_('layout_note'), db_column='layout_note', max_length=255, null=True, blank=True)
    room_area = models.DecimalField(_('room_area'), db_column='room_area', default=0, max_digits=5, decimal_places=2)

    direction = models.ForeignKey(
        Direction,
        db_column='direction_id',
        related_name='searched_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    rent = models.IntegerField(_('rent'), db_column='rent', db_index=True, default=0)
    rent_upper = models.IntegerField(_('rent_upper'), db_column='rent_upper', db_index=True, default=0)
    rent_tax_type = models.ForeignKey(
        TaxType,
        db_column='rent_tax_type_id',
        related_name='rent_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    rent_hidden = models.BooleanField(_('rent_hidden'), db_column='rent_hidden', default=False)
    condo_fees_type = models.ForeignKey(
        CondoFeesType,
        db_column='condo_fees_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    condo_fees = models.IntegerField(_('condo_fees'), db_column='condo_fees', default=0)
    condo_fees_tax_type = models.ForeignKey(
        TaxType,
        db_column='condo_fees_tax_type_id',
        related_name='condo_fees_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    water_cost_type = models.ForeignKey(
        WaterCostType,
        db_column='water_cost_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    water_cost = models.IntegerField(_('water_cost'), db_column='water_cost', default=0)
    water_cost_tax_type = models.ForeignKey(
        TaxType,
        db_column='water_cost_tax_type_id',
        related_name='water_cost_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_type1 = models.ForeignKey(
        DepositType,
        db_column='deposit_type_id1',
        related_name='deposit_type_searched_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_notation1 = models.ForeignKey(
        DepositNotation,
        db_column='deposit_notation_id1',
        related_name='deposit_notation_searched_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_value1 = models.DecimalField(_('deposit_value1'), db_column='deposit_value1', default=0, max_digits=12, decimal_places=2)
    deposit_tax_type1 = models.ForeignKey(
        TaxType,
        db_column='deposit_tax_type_id1',
        related_name='deposit_searched_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_comment1 = models.CharField(_('deposit_comment1'), db_column='deposit_comment1', max_length=100, null=True, blank=True)
    deposit_type2 = models.ForeignKey(
        DepositType,
        db_column='deposit_type_id2',
        related_name='deposit_type_searched_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_notation2 = models.ForeignKey(
        DepositNotation,
        db_column='deposit_notation_id2',
        related_name='deposit_notation_searched_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_value2 = models.DecimalField(_('deposit_value2'), db_column='deposit_value2', default=0, max_digits=12, decimal_places=2)
    deposit_tax_type2 = models.ForeignKey(
        TaxType,
        db_column='deposit_tax_type_id2',
        related_name='deposit_searched_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_comment2 = models.CharField(_('deposit_comment2'), db_column='deposit_comment2', max_length=100, null=True, blank=True)
    key_money_type1 = models.ForeignKey(
        KeyMoneyType,
        db_column='key_money_type_id1',
        related_name='key_money_type_searched_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_notation1 = models.ForeignKey(
        KeyMoneyNotation,
        db_column='key_money_notation_id1',
        related_name='key_money_notation_searched_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_value1 = models.DecimalField(_('key_money_value1'), db_column='key_money_value1', default=0, max_digits=12, decimal_places=2)
    key_money_tax_type1 = models.ForeignKey(
        TaxType,
        db_column='key_money_tax_type_id1',
        related_name='key_money_searched_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_comment1 = models.CharField(_('key_money_comment1'), db_column='key_money_comment1', max_length=100, null=True, blank=True)
    key_money_type2 = models.ForeignKey(
        KeyMoneyType,
        db_column='key_money_type_id2',
        related_name='key_money_type_searched_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_notation2 = models.ForeignKey(
        KeyMoneyNotation,
        db_column='key_money_notation_id2',
        related_name='key_money_notation_searched_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_value2 = models.DecimalField(_('key_money_value2'), db_column='key_money_value2', default=0, max_digits=12, decimal_places=2)
    key_money_tax_type2 = models.ForeignKey(
        TaxType,
        db_column='key_money_tax_type_id2',
        related_name='key_money_searched_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_comment2 = models.CharField(_('key_money_comment2'), db_column='key_money_comment2', max_length=100, null=True, blank=True)
    contract_years = models.IntegerField(_('contract_years'), db_column='contract_years', default=0)
    contract_months = models.IntegerField(_('contract_months'), db_column='contract_months', default=0)
    renewal_fee_notation = models.ForeignKey(
        RenewalFeeNotation,
        db_column='renewal_fee_notation_id',
        related_name='renewal_fee_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    renewal_fee_value = models.DecimalField(_('renewal_fee_value'), db_column='renewal_fee_value', default=0, max_digits=12, decimal_places=2)
    renewal_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='renewal_fee_tax_type_id',
        related_name='renewal_fee_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    is_auto_renewal = models.BooleanField(_('is_auto_renewal'), db_column='is_auto_renewal', default=False)
    insurance_type = models.ForeignKey(
        InsuranceType,
        db_column='insurance_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    insurance_years = models.IntegerField(_('insurance_years'), db_column='insurance_years', default=0)
    insurance_fee = models.IntegerField(_('insurance_fee'), db_column='insurance_fee', default=0)
    insurance_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='insurance_fee_tax_type_id',
        related_name='insurance_fee_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    guarantee_type = models.ForeignKey(
        GuaranteeType,
        db_column='guarantee_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    free_rent_type = models.ForeignKey(
        FreeRentType,
        db_column='free_rent_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    free_rent_months = models.IntegerField(_('free_rent_months'), db_column='free_rent_months', default=0)
    free_rent_limit_year = models.IntegerField(_('free_rent_limit_year'), db_column='free_rent_limit_year', default=0)
    free_rent_limit_month = models.IntegerField(_('free_rent_limit_month'), db_column='free_rent_limit_month', default=0)

    gas_type = models.ForeignKey(
        GasType,
        db_column='gas_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    bath_type = models.ForeignKey(
        BathType,
        db_column='bath_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    toilet_type = models.ForeignKey(
        ToiletType,
        db_column='toilet_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    kitchen_range_type = models.ForeignKey(
        KitchenRangeType,
        db_column='kitchen_range_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    internet_type = models.ForeignKey(
        InternetType,
        db_column='internet_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    washer_type = models.ForeignKey(
        WasherType,
        db_column='washer_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    pet_type = models.ForeignKey(
        PetType,
        db_column='pet_type_id',
        related_name='searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    instrument_type = models.ForeignKey(
        AllowType,
        db_column='instrument_type_id',
        related_name='instrument_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    live_together_type = models.ForeignKey(
        AllowType,
        db_column='live_together_type_id',
        related_name='live_together_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    share_type = models.ForeignKey(
        AllowType,
        db_column='share_type_id',
        related_name='share_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    non_japanese_type = models.ForeignKey(
        AllowType,
        db_column='non_japanese_type_id',
        related_name='non_japanese_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    only_woman_type = models.ForeignKey(
        AllowType,
        db_column='only_woman_type_id',
        related_name='only_woman_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    only_man_type = models.ForeignKey(
        AllowType,
        db_column='only_man_type_id',
        related_name='only_man_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    new_student_type = models.ForeignKey(
        AllowType,
        db_column='new_student_type_id',
        related_name='new_student_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    office_use_type = models.ForeignKey(
        AllowType,
        db_column='office_use_type_id',
        related_name='office_use_searched_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    reform_comment = models.CharField(_('reform_comment'), db_column='reform_comment', max_length=100, null=True, blank=True)
    reform_year = models.IntegerField(_('reform_year'), db_column='reform_year', default=0)
    reform_month = models.IntegerField(_('reform_month'), db_column='reform_month', default=0)

    web_catch_copy = models.CharField(_('web_catch_copy'), db_column='web_catch_copy', max_length=100, null=True, blank=True)
    web_appeal = models.CharField(_('web_appeal'), db_column='web_appeal', max_length=255, null=True, blank=True)
    building_web_catch_copy = models.CharField(_('building_web_catch_copy'), db_column='building_web_catch_copy', max_length=100, null=True, blank=True)
    building_web_appeal = models.CharField(_('building_web_appeal'), db_column='building_web_appeal', max_length=255, null=True, blank=True)

    has_panoramas = models.BooleanField(_('has_panoramas'), db_column='has_panoramas', default=False)
    has_movies = models.BooleanField(_('has_movies'), db_column='has_movies', default=False)

    class Meta:
        managed = False

    """
    検索関連
    """
    @classmethod
    def get_rooms(cls, conditions: SearchConditions, is_residential):
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
        ans = 'room.id'
        ans += ', room.oid'
        ans += ', room.building_id'
        ans += ', building.oid AS building_oid'
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

        ans += ', room.room_no'
        ans += ', room.room_floor'
        ans += ', room.rental_type_id'
        ans += ', room.room_status_id'
        ans += ', room.vacancy_status_id'
        ans += ', room.layout_type_id'
        ans += ', room.western_style_room1'
        ans += ', room.western_style_room2'
        ans += ', room.western_style_room3'
        ans += ', room.western_style_room4'
        ans += ', room.western_style_room5'
        ans += ', room.western_style_room6'
        ans += ', room.western_style_room7'
        ans += ', room.western_style_room8'
        ans += ', room.western_style_room9'
        ans += ', room.western_style_room10'
        ans += ', room.japanese_style_room1'
        ans += ', room.japanese_style_room2'
        ans += ', room.japanese_style_room3'
        ans += ', room.japanese_style_room4'
        ans += ', room.japanese_style_room5'
        ans += ', room.japanese_style_room6'
        ans += ', room.japanese_style_room7'
        ans += ', room.japanese_style_room8'
        ans += ', room.japanese_style_room9'
        ans += ', room.japanese_style_room10'
        ans += ', room.kitchen_type_id1'
        ans += ', room.kitchen1'
        ans += ', room.kitchen_type_id2'
        ans += ', room.kitchen2'
        ans += ', room.kitchen_type_id3'
        ans += ', room.kitchen3'
        ans += ', room.store_room1'
        ans += ', room.store_room2'
        ans += ', room.store_room3'
        ans += ', room.loft1'
        ans += ', room.loft2'
        ans += ', room.sun_room1'
        ans += ', room.sun_room2'
        ans += ', room.layout_note'
        ans += ', room.room_area'
        ans += ', room.direction_id'
        ans += ', room.rent'
        ans += ', room.rent_upper'
        ans += ', room.rent_tax_type_id'
        ans += ', room.rent_hidden'
        ans += ', room.condo_fees_type_id'
        ans += ', room.condo_fees'
        ans += ', room.condo_fees_tax_type_id'
        ans += ', room.water_cost_type_id'
        ans += ', room.water_cost'
        ans += ', room.water_cost_tax_type_id'
        ans += ', room.deposit_type_id1'
        ans += ', room.deposit_notation_id1'
        ans += ', room.deposit_value1'
        ans += ', room.deposit_tax_type_id1'
        ans += ', room.deposit_comment1'
        ans += ', room.deposit_type_id2'
        ans += ', room.deposit_notation_id2'
        ans += ', room.deposit_value2'
        ans += ', room.deposit_tax_type_id2'
        ans += ', room.deposit_comment2'
        ans += ', room.key_money_type_id1'
        ans += ', room.key_money_notation_id1'
        ans += ', room.key_money_value1'
        ans += ', room.key_money_tax_type_id1'
        ans += ', room.key_money_comment1'
        ans += ', room.key_money_type_id2'
        ans += ', room.key_money_notation_id2'
        ans += ', room.key_money_value2'
        ans += ', room.key_money_tax_type_id2'
        ans += ', room.key_money_comment2'
        ans += ', room.contract_years'
        ans += ', room.contract_months'
        ans += ', room.renewal_fee_notation_id'
        ans += ', room.renewal_fee_value'
        ans += ', room.renewal_fee_tax_type_id'
        ans += ', room.is_auto_renewal'
        ans += ', room.insurance_type_id'
        ans += ', room.insurance_years'
        ans += ', room.insurance_fee'
        ans += ', room.insurance_fee_tax_type_id'
        ans += ', room.guarantee_type_id'
        ans += ', room.free_rent_type_id'
        ans += ', room.free_rent_months'
        ans += ', room.free_rent_limit_year'
        ans += ', room.free_rent_limit_month'
        ans += ', room.gas_type_id'
        ans += ', room.bath_type_id'
        ans += ', room.toilet_type_id'
        ans += ', room.kitchen_range_type_id'
        ans += ', room.internet_type_id'
        ans += ', room.washer_type_id'
        ans += ', room.pet_type_id'
        ans += ', room.instrument_type_id'
        ans += ', room.live_together_type_id'
        ans += ', room.share_type_id'
        ans += ', room.non_japanese_type_id'
        ans += ', room.only_woman_type_id'
        ans += ', room.only_man_type_id'
        ans += ', room.new_student_type_id'
        ans += ', room.office_use_type_id'
        ans += ', room.reform_comment'
        ans += ', room.reform_year'
        ans += ', room.reform_month'

        ans += ', room.web_catch_copy'
        ans += ', room.web_appeal'
        ans += ', building.web_catch_copy AS building_web_catch_copy'
        ans += ', building.web_appeal AS building_web_appeal'

        ans += ', CASE WHEN panoramas.room_id IS NULL THEN FALSE'
        ans += ' WHEN panoramas.panorama_count > 0 THEN TRUE'
        ans += ' ELSE FALSE END AS has_panoramas'
        ans += ', CASE WHEN movies.room_id IS NULL THEN FALSE'
        ans += ' WHEN movies.movie_count > 0 THEN TRUE'
        ans += ' ELSE FALSE END AS has_movies'

        return ans

    @classmethod
    def __get_sql_tables(cls, conditions: SearchConditions, params, is_residential):
        """SQLのテーブル一覧"""
        ans = 'room'
        ans += ' INNER JOIN room_status ON room.room_status_id = room_status.id AND room_status.for_rent = TRUE'
        ans += ' INNER JOIN building ON room.building_id = building.id'
        ans += ' INNER JOIN building_type ON building.building_type_id = building_type.id'
        if is_residential:
            ans += ' AND building_type.is_residential = TRUE'
        else:
            ans += ' AND building_type.is_building = TRUE'
        ans += ' INNER JOIN rental_type ON room.rental_type_id = rental_type.id'
        if is_residential:
            ans += ' AND rental_type.is_residential = TRUE'
        else:
            ans += ' AND rental_type.is_non_residential = TRUE'
        ans += ' INNER JOIN garage_type ON building.garage_type_id = garage_type.id'
        ans += ' INNER JOIN bike_parking_type ON building.bike_parking_type_id = bike_parking_type.id'
        ans += ' INNER JOIN pref ON building.pref_id = pref.id'
        ans += ' INNER JOIN city ON building.city_id = city.id'
        ans += ' INNER JOIN pet_type on room.pet_type_id = pet_type.id'

        if conditions:
            # 管理種別の限定有無
            ans += xstr(conditions.get_no_limit_sql(is_building=False))

            # ランドマーク
            ans += xstr(conditions.get_landmarks_sql(params=params))

            # 設備条件
            ans += xstr(conditions.get_only_top_floor_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_system_kitchen_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_washstand_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_aircon_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_auto_lock_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_designers_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_elevator_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_delivery_box_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_reheating_bath_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_washing_toilet_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_tv_intercom_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_loft_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_renovation_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_diy_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_walk_in_closet_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_barrier_free_sql(is_building=False, is_residential=is_residential))
            ans += xstr(conditions.get_garbage_box_24_sql(is_building=False, is_residential=is_residential))
            if not is_residential:
                ans += xstr(conditions.get_tenant_furnished_shop_sql(is_building=False))
                ans += xstr(conditions.get_tenant_skeleton_sql(is_building=False))
                ans += xstr(conditions.get_tenant_restaurant_sql(is_building=False))
                ans += xstr(conditions.get_tenant_office_sql(is_building=False))
                ans += xstr(conditions.get_tenant_first_floor_sql(is_building=False))
                ans += xstr(conditions.get_tenant_soho_sql(is_building=False))
                ans += xstr(conditions.get_tenant_residence_sql(is_building=False))

            # 新着順
            ans += xstr(conditions.get_new_arrival_sql(is_building=False, is_residential=is_residential))

        ans += ' LEFT JOIN ('
        ans += 'SELECT room_panorama.room_id'
        ans += ', COUNT(room_panorama.id) AS panorama_count'
        ans += ' FROM room_panorama'
        ans += ' WHERE room_panorama.is_deleted = FALSE'
        ans += ' AND room_panorama.is_publish_web = TRUE'
        ans += ' GROUP BY room_panorama.room_id'
        ans += ') panoramas ON panoramas.room_id = room.id'

        ans += ' LEFT JOIN ('
        ans += 'SELECT room_movie.room_id'
        ans += ', COUNT(room_movie.id) AS movie_count'
        ans += ' FROM room_movie'
        ans += ' WHERE room_movie.is_deleted = FALSE'
        ans += ' AND room_movie.is_publish_web = TRUE'
        ans += ' GROUP BY room_movie.room_id'
        ans += ') movies ON movies.room_id = room.id'

        return ans

    @classmethod
    def __get_sql_conditions(cls, conditions: SearchConditions, params):
        """SQLの条件一覧"""
        ans = 'room.is_deleted = FALSE'
        ans += ' AND room.is_publish_web = TRUE'
        ans += ' AND building.is_deleted = FALSE'
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
        ans += ', pref.priority, city.priority, building.building_kana, room.room_no, room.id'

        return ans

    """
    プロパティ
    """
    @property
    def exterior_picture(self):
        return SearchedBuildingExteriorPicture.get_picture(self.building_id)

    @property
    def interior_picture(self):
        return SearchedRoomInteriorPicture.get_picture(self.id)

    @property
    def layout_picture(self):
        return SearchedRoomLayoutPicture.get_picture(self.id)

    @property
    def equipments(self):
        return SearchedRoomEquipment.get_equipments(self.id)

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

    @property
    def room_floor_text(self):
        return DataHelper.get_room_floor_text(self.room_floor)

    @property
    def rent_text(self):
        return DataHelper.get_rent_text(
            self.rent_hidden,
            self.rent,
            self.rent_upper,
            self.rent_tax_type)

    @property
    def condo_fees_text(self):
        return DataHelper.get_condo_fees_text(
            self.condo_fees_type,
            self.condo_fees,
            self.condo_fees_tax_type)

    @property
    def water_cost_text(self):
        return DataHelper.get_water_cost_text(
            self.water_cost_type,
            self.water_cost,
            self.water_cost_tax_type)

    @property
    def free_rent_text(self):
        return DataHelper.get_free_rent_text(
            self.free_rent_type,
            self.free_rent_months,
            self.free_rent_limit_year,
            self.free_rent_limit_month)

    @property
    def deposit_type_text1(self):
        return DataHelper.get_deposit_type_text(self.deposit_type1)

    @property
    def deposit_text1(self):
        return DataHelper.get_deposit_text(
            self.deposit_type1,
            self.deposit_notation1,
            self.deposit_value1,
            self.deposit_tax_type1)

    @property
    def deposit_type_text2(self):
        return DataHelper.get_deposit_type_text(self.deposit_type2)

    @property
    def deposit_text2(self):
        return DataHelper.get_deposit_text(
            self.deposit_type2,
            self.deposit_notation2,
            self.deposit_value2,
            self.deposit_tax_type2)

    @property
    def key_money_type_text1(self):
        return DataHelper.get_key_money_type_text(self.key_money_type1)

    @property
    def key_money_text1(self):
        return DataHelper.get_key_money_text(
            self.key_money_type1,
            self.key_money_notation1,
            self.key_money_value1,
            self.key_money_tax_type1)

    @property
    def key_money_type_text2(self):
        return DataHelper.get_key_money_type_text(self.key_money_type2)

    @property
    def key_money_text2(self):
        return DataHelper.get_key_money_text(
            self.key_money_type2,
            self.key_money_notation2,
            self.key_money_value2,
            self.key_money_tax_type2)

    @property
    def insurance_type_text(self):
        return DataHelper.get_insurance_type_text(self.insurance_type)

    @property
    def insurance_text(self):
        return DataHelper.get_insurance_text(
            self.insurance_type,
            self.insurance_years,
            self.insurance_fee,
            self.insurance_fee_tax_type)

    @property
    def guarantee_type_text(self):
        return DataHelper.get_guarantee_type_text(self.guarantee_type)

    @property
    def rental_type_text(self):
        return DataHelper.get_rental_type_text(self.rental_type)

    @property
    def rental_type_short_text(self):
        return DataHelper.get_rental_type_short_text(self.rental_type)

    @property
    def contract_span_text(self):
        return DataHelper.get_contract_span_text(
            self.contract_years,
            self.contract_months,
            self.is_auto_renewal)

    @property
    def renewal_fee_text(self):
        return DataHelper.get_renewal_fee_text(
            self.renewal_fee_notation,
            self.renewal_fee_value,
            self.renewal_fee_tax_type)

    @property
    def room_area_text(self):
        return DataHelper.get_room_area_text(self.room_area)

    @property
    def layout_type_text(self):
        return DataHelper.get_layout_type_text(self.layout_type)

    @property
    def layout_detail_text(self):
        return DataHelper.get_layout_detail_text(self)

    @property
    def direction_text(self):
        return DataHelper.get_direction_text(self.direction)

    @property
    def room_status_text(self):
        return DataHelper.get_room_status_text(self.room_status)

    @property
    def vacancy_status_text(self):
        return DataHelper.get_vacancy_status_text(
            self.room_status,
            self.vacancy_status)

    @property
    def reform_year_month(self):
        return DataHelper.get_reform_year_month(
            self.reform_year,
            self.reform_month)
    @property
    def gas_text(self):
        return DataHelper.get_gas_text(self.gas_type)

    @property
    def bath_text(self):
        return DataHelper.get_bath_text(self.bath_type)

    @property
    def toilet_text(self):
        return DataHelper.get_toilet_text(self.toilet_type)

    @property
    def kitchen_range_text(self):
        return DataHelper.get_kitchen_range_text(self.kitchen_range_type)

    @property
    def internet_text(self):
        return DataHelper.get_internet_text(self.internet_type)

    @property
    def washer_text(self):
        return DataHelper.get_washer_text(self.washer_type)

    @property
    def pet_text(self):
        return DataHelper.get_pet_text(self.pet_type)

    @property
    def instrument_type_text(self):
        return DataHelper.get_allow_type_text(self.instrument_type)

    @property
    def live_together_type_text(self):
        return DataHelper.get_allow_type_text(self.live_together_type)

    @property
    def share_type_text(self):
        return DataHelper.get_allow_type_text(self.share_type)

    @property
    def non_japanese_type_text(self):
        return DataHelper.get_allow_type_text(self.non_japanese_type)

    @property
    def only_woman_type_text(self):
        return DataHelper.get_allow_type_text(self.only_woman_type)

    @property
    def only_man_type_text(self):
        return DataHelper.get_allow_type_text(self.only_man_type)

    @property
    def new_student_type_text(self):
        return DataHelper.get_allow_type_text(self.new_student_type)

    @property
    def office_use_type_text(self):
        return DataHelper.get_allow_type_text(self.office_use_type)

    @property
    def equipments_text(self):
        ans = ''
        for item in self.equipments:
            if ans != '':
                ans += '・'
            ans += item.name

        if ans == '':
            ans = None

        return ans

    @property
    def equipments_short_text(self):
        ans = ''
        for item in self.equipments:
            if ans != '':
                ans += '・'
            ans += item.short_name

        if ans == '':
            ans = None

        return ans
