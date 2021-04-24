"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.db import models
from django.db.models import Q
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lib.convert import *
from lib.functions import *
from lib.data_helper import DataHelper
from .allow_type import AllowType
from .balcony_type import BalconyType
from .bath_type import BathType
from .cleaning_type import CleaningType
from .condo_fees_type import CondoFeesType
from .deposit_notation import DepositNotation
from .deposit_type import DepositType
from .direction import Direction
from .electric_type import ElectricType
from .existence import Existence
from .free_rent_type import FreeRentType
from .gas_type import GasType
from .guarantee_type import GuaranteeType
from .insurance_type import InsuranceType
from .internet_type import InternetType
from .key_money_notation import KeyMoneyNotation
from .key_money_type import KeyMoneyType
from .kitchen_type import KitchenType
from .kitchen_range_type import KitchenRangeType
from .layout_type import LayoutType
from .month_day import MonthDay
from .payment_fee_type import PaymentFeeType
from .payment_type import PaymentType
from .pet_type import PetType
from .renewal_fee_notation import RenewalFeeNotation
from .rental_type import RentalType
from .room_status import RoomStatus
from .tax_type import TaxType
from .toilet_type import ToiletType
from .trader import Trader
from .vacancy_status import VacancyStatus
from .washer_type import WasherType
from .water_cost_type import WaterCostType


class Room(models.Model):
    """
    部屋
    """
    is_no_limit = False         # 自社物件以外も含む場合はTrue
    is_only_residential = False      # 居住用のみ対象の場合はTrue
    is_only_non_residential = False  # 非居住用のみ対象の場合はTrue

    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    oid = models.CharField(_('oid'), db_column='oid', db_index=True, unique=True, max_length=50)
    building = models.ForeignKey(
        'Building',
        db_column='building_id',
        related_name='rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )

    room_no = models.CharField(_('room_no'), db_column='room_no', max_length=20, db_index=True, null=True, blank=True)
    room_floor = models.IntegerField(_('room_floor'), db_column='room_floor', default=0)
    rental_type = models.ForeignKey(
        RentalType,
        db_column='rental_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    is_sublease = models.BooleanField(_('is_sublease'), db_column='is_sublease', db_index=True, default=False)

    is_condo_management = models.BooleanField(_('is_condo_management'), db_column='is_condo_management', db_index=True, default=False)
    is_entrusted = models.BooleanField(_('is_entrusted'), db_column='is_entrusted', db_index=True, default=False)
    condo_trader = models.ForeignKey(
        Trader,
        db_column='condo_trader_id',
        related_name='condo_rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )

    room_status = models.ForeignKey(
        RoomStatus,
        db_column='room_status_id',
        related_name='rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    vacancy_status = models.ForeignKey(
        VacancyStatus,
        db_column='vacancy_status_id',
        related_name='rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    vacancy_status_note = models.TextField(_('vacancy_status_note'), db_column='vacancy_status_note', max_length=2000, null=True, blank=True)

    live_start_year = models.IntegerField(_('live_start_year'), db_column='live_start_year', default=0)
    live_start_month = models.IntegerField(_('live_start_month'), db_column='live_start_month', default=0)
    live_start_day = models.ForeignKey(
        MonthDay,
        db_column='live_start_day_id',
        related_name='live_start_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    live_start_note = models.CharField(_('live_start_note'), db_column='live_start_note', max_length=255, null=True, blank=True)
    cancel_scheduled_year = models.IntegerField(_('cancel_scheduled_year'), db_column='cancel_scheduled_year', default=0)
    cancel_scheduled_month = models.IntegerField(_('cancel_scheduled_month'), db_column='cancel_scheduled_month', default=0)
    cancel_scheduled_day = models.ForeignKey(
        MonthDay,
        db_column='cancel_scheduled_day_id',
        related_name='cancel_scheduled_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    cancel_scheduled_note = models.CharField(_('cancel_scheduled_note'), db_column='cancel_scheduled_note', max_length=255, null=True, blank=True)

    is_publish_web = models.BooleanField(_('is_publish_web'), db_column='is_publish_web', db_index=True, default=True)
    web_catch_copy = models.CharField(_('web_catch_copy'), db_column='web_catch_copy', max_length=100, null=True, blank=True)
    web_appeal = models.CharField(_('web_appeal'), db_column='web_appeal', max_length=255, null=True, blank=True)
    web_note = models.TextField(_('web_note'), db_column='web_note', max_length=2000, null=True, blank=True)

    layout_type = models.ForeignKey(
        LayoutType,
        db_column='layout_type_id',
        related_name='rooms',
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
        related_name='rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    kitchen1 = models.DecimalField(_('kitchen1'), db_column='kitchen1', default=0, max_digits=5, decimal_places=2)
    kitchen_type2 = models.ForeignKey(
        KitchenType,
        db_column='kitchen_type_id2',
        related_name='rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    kitchen2 = models.DecimalField(_('kitchen2'), db_column='kitchen2', default=0, max_digits=5, decimal_places=2)
    kitchen_type3 = models.ForeignKey(
        KitchenType,
        db_column='kitchen_type_id3',
        related_name='rooms3',
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
        related_name='rooms',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    balcony_type = models.ForeignKey(
        BalconyType,
        db_column='balcony_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    balcony_area = models.DecimalField(_('balcony_area'), db_column='balcony_area', default=0, max_digits=5, decimal_places=2)
    rent = models.IntegerField(_('rent'), db_column='rent', db_index=True, default=0)
    rent_upper = models.IntegerField(_('rent_upper'), db_column='rent_upper', db_index=True, default=0)
    rent_tax_type = models.ForeignKey(
        TaxType,
        db_column='rent_tax_type_id',
        related_name='rent_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    rent_hidden = models.BooleanField(_('rent_hidden'), db_column='rent_hidden', default=False)
    condo_fees_type = models.ForeignKey(
        CondoFeesType,
        db_column='condo_fees_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    condo_fees = models.IntegerField(_('condo_fees'), db_column='condo_fees', default=0)
    condo_fees_tax_type = models.ForeignKey(
        TaxType,
        db_column='condo_fees_tax_type_id',
        related_name='condo_fees_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    water_cost_type = models.ForeignKey(
        WaterCostType,
        db_column='water_cost_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    water_cost = models.IntegerField(_('water_cost'), db_column='water_cost', default=0)
    water_cost_tax_type = models.ForeignKey(
        TaxType,
        db_column='water_cost_tax_type_id',
        related_name='water_cost_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    payment_type = models.ForeignKey(
        PaymentType,
        db_column='payment_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    payment_fee_type = models.ForeignKey(
        PaymentFeeType,
        db_column='payment_fee_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    payment_fee = models.IntegerField(_('payment_fee'), db_column='payment_fee', default=0)
    payment_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='payment_fee_tax_type_id',
        related_name='payment_fee_rooms',
        on_delete=models.PROTECT,
        default=0,
    )

    monthly_cost_name1 = models.CharField(_('monthly_cost_name1'), db_column='monthly_cost_name1', max_length=100, null=True, blank=True)
    monthly_cost1 = models.IntegerField(_('monthly_cost1'), db_column='monthly_cost1', default=0)
    monthly_cost_tax_type1 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id1',
        related_name='monthly_cost_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_name2 = models.CharField(_('monthly_cost_name2'), db_column='monthly_cost_name2', max_length=100, null=True, blank=True)
    monthly_cost2 = models.IntegerField(_('monthly_cost2'), db_column='monthly_cost2', default=0)
    monthly_cost_tax_type2 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id2',
        related_name='monthly_cost_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_name3 = models.CharField(_('monthly_cost_name3'), db_column='monthly_cost_name3', max_length=100, null=True, blank=True)
    monthly_cost3 = models.IntegerField(_('monthly_cost3'), db_column='monthly_cost3', default=0)
    monthly_cost_tax_type3 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id3',
        related_name='monthly_cost_rooms3',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_name4 = models.CharField(_('monthly_cost_name4'), db_column='monthly_cost_name4', max_length=100, null=True, blank=True)
    monthly_cost4 = models.IntegerField(_('monthly_cost4'), db_column='monthly_cost4', default=0)
    monthly_cost_tax_type4 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id4',
        related_name='monthly_cost_rooms4',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_name5 = models.CharField(_('monthly_cost_name5'), db_column='monthly_cost_name5', max_length=100, null=True, blank=True)
    monthly_cost5 = models.IntegerField(_('monthly_cost5'), db_column='monthly_cost5', default=0)
    monthly_cost_tax_type5 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id5',
        related_name='monthly_cost_rooms5',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_name6 = models.CharField(_('monthly_cost_name6'), db_column='monthly_cost_name6', max_length=100, null=True, blank=True)
    monthly_cost6 = models.IntegerField(_('monthly_cost6'), db_column='monthly_cost6', default=0)
    monthly_cost_tax_type6 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id6',
        related_name='monthly_cost_rooms6',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_name7 = models.CharField(_('monthly_cost_name7'), db_column='monthly_cost_name7', max_length=100, null=True, blank=True)
    monthly_cost7 = models.IntegerField(_('monthly_cost7'), db_column='monthly_cost7', default=0)
    monthly_cost_tax_type7 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id7',
        related_name='monthly_cost_rooms7',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_name8 = models.CharField(_('monthly_cost_name8'), db_column='monthly_cost_name8', max_length=100, null=True, blank=True)
    monthly_cost8 = models.IntegerField(_('monthly_cost8'), db_column='monthly_cost8', default=0)
    monthly_cost_tax_type8 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id8',
        related_name='monthly_cost_rooms8',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_name9 = models.CharField(_('monthly_cost_name9'), db_column='monthly_cost_name9', max_length=100, null=True, blank=True)
    monthly_cost9 = models.IntegerField(_('monthly_cost9'), db_column='monthly_cost9', default=0)
    monthly_cost_tax_type9 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id9',
        related_name='monthly_cost_rooms9',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_name10 = models.CharField(_('monthly_cost_name10'), db_column='monthly_cost_name10', max_length=100, null=True, blank=True)
    monthly_cost10 = models.IntegerField(_('monthly_cost10'), db_column='monthly_cost10', default=0)
    monthly_cost_tax_type10 = models.ForeignKey(
        TaxType,
        db_column='monthly_cost_tax_type_id10',
        related_name='monthly_cost_rooms10',
        on_delete=models.PROTECT,
        default=0,
    )
    monthly_cost_note = models.TextField(_('monthly_cost_note'), db_column='monthly_cost_note', max_length=2000, null=True, blank=True)
    deposit_type1 = models.ForeignKey(
        DepositType,
        db_column='deposit_type_id1',
        related_name='deposit_type_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_notation1 = models.ForeignKey(
        DepositNotation,
        db_column='deposit_notation_id1',
        related_name='deposit_notation_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_value1 = models.DecimalField(_('deposit_value1'), db_column='deposit_value1', default=0, max_digits=12, decimal_places=2)
    deposit_tax_type1 = models.ForeignKey(
        TaxType,
        db_column='deposit_tax_type_id1',
        related_name='deposit_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_comment1 = models.CharField(_('deposit_comment1'), db_column='deposit_comment1', max_length=100, null=True, blank=True)
    deposit_type2 = models.ForeignKey(
        DepositType,
        db_column='deposit_type_id2',
        related_name='deposit_type_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_notation2 = models.ForeignKey(
        DepositNotation,
        db_column='deposit_notation_id2',
        related_name='deposit_notation_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_value2 = models.DecimalField(_('deposit_value2'), db_column='deposit_value2', default=0, max_digits=12, decimal_places=2)
    deposit_tax_type2 = models.ForeignKey(
        TaxType,
        db_column='deposit_tax_type_id2',
        related_name='deposit_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    deposit_comment2 = models.CharField(_('deposit_comment2'), db_column='deposit_comment2', max_length=100, null=True, blank=True)
    key_money_type1 = models.ForeignKey(
        KeyMoneyType,
        db_column='key_money_type_id1',
        related_name='key_money_type_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_notation1 = models.ForeignKey(
        KeyMoneyNotation,
        db_column='key_money_notation_id1',
        related_name='key_money_notation_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_value1 = models.DecimalField(_('key_money_value1'), db_column='key_money_value1', default=0, max_digits=12, decimal_places=2)
    key_money_tax_type1 = models.ForeignKey(
        TaxType,
        db_column='key_money_tax_type_id1',
        related_name='key_money_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_comment1 = models.CharField(_('key_money_comment1'), db_column='key_money_comment1', max_length=100, null=True, blank=True)
    key_money_type2 = models.ForeignKey(
        KeyMoneyType,
        db_column='key_money_type_id2',
        related_name='key_money_type_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_notation2 = models.ForeignKey(
        KeyMoneyNotation,
        db_column='key_money_notation_id2',
        related_name='key_money_notation_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_value2 = models.DecimalField(_('key_money_value2'), db_column='key_money_value2', default=0, max_digits=12, decimal_places=2)
    key_money_tax_type2 = models.ForeignKey(
        TaxType,
        db_column='key_money_tax_type_id2',
        related_name='key_money_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    key_money_comment2 = models.CharField(_('key_money_comment2'), db_column='key_money_comment2', max_length=100, null=True, blank=True)
    contract_years = models.IntegerField(_('contract_years'), db_column='contract_years', default=0)
    contract_months = models.IntegerField(_('contract_months'), db_column='contract_months', default=0)
    renewal_fee_notation = models.ForeignKey(
        RenewalFeeNotation,
        db_column='renewal_fee_notation_id',
        related_name='renewal_fee_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    renewal_fee_value = models.DecimalField(_('renewal_fee_value'), db_column='renewal_fee_value', default=0, max_digits=12, decimal_places=2)
    renewal_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='renewal_fee_tax_type_id',
        related_name='renewal_fee_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    renewal_charge_existence = models.ForeignKey(
        Existence,
        db_column='renewal_charge_existence_id',
        related_name='renewal_charge_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    renewal_charge = models.IntegerField(_('renewal_charge'), db_column='renewal_charge', default=0)
    renewal_charge_tax_type = models.ForeignKey(
        TaxType,
        db_column='renewal_charge_tax_type_id',
        related_name='renewal_charge_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    is_auto_renewal = models.BooleanField(_('is_auto_renewal'), db_column='is_auto_renewal', default=False)
    renewal_note = models.CharField(_('renewal_note'), db_column='renewal_note', max_length=255, null=True, blank=True)
    recontract_fee_existence = models.ForeignKey(
        Existence,
        db_column='recontract_fee_existence_id',
        related_name='recontract_fee_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    recontract_fee = models.IntegerField(_('recontract_fee'), db_column='recontract_fee', default=0)
    recontract_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='recontract_fee_tax_type_id',
        related_name='recontract_fee_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    recontract_note = models.CharField(_('recontract_note'), db_column='recontract_note', max_length=255, null=True, blank=True)

    insurance_type = models.ForeignKey(
        InsuranceType,
        db_column='insurance_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    insurance_company = models.CharField(_('insurance_company'), db_column='insurance_company', max_length=100, null=True, blank=True)
    insurance_years = models.IntegerField(_('insurance_years'), db_column='insurance_years', default=0)
    insurance_fee = models.IntegerField(_('insurance_fee'), db_column='insurance_fee', default=0)
    insurance_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='insurance_fee_tax_type_id',
        related_name='insurance_fee_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    guarantee_type = models.ForeignKey(
        GuaranteeType,
        db_column='guarantee_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    guarantee_company = models.CharField(_('guarantee_company'), db_column='guarantee_company', max_length=100, null=True, blank=True)
    guarantee_fee = models.CharField(_('guarantee_fee'), db_column='guarantee_fee', max_length=255, null=True, blank=True)

    document_cost_existence = models.ForeignKey(
        Existence,
        db_column='document_cost_existence_id',
        related_name='document_cost_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    document_cost = models.IntegerField(_('document_cost'), db_column='document_cost', default=0)
    document_cost_tax_type = models.ForeignKey(
        TaxType,
        db_column='document_cost_tax_type_id',
        related_name='document_cost_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    document_cost_comment = models.CharField(_('document_cost_comment'), db_column='document_cost_comment', max_length=100, null=True, blank=True)
    key_change_cost_existence = models.ForeignKey(
        Existence,
        db_column='key_change_cost_existence_id',
        related_name='key_change_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    key_change_cost = models.IntegerField(_('key_change_cost'), db_column='key_change_cost', default=0)
    key_change_cost_tax_type = models.ForeignKey(
        TaxType,
        db_column='key_change_cost_tax_type_id',
        related_name='key_change_cost_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    key_change_comment = models.CharField(_('key_change_comment'), db_column='key_change_comment', max_length=100, null=True, blank=True)

    initial_cost_name1 = models.CharField(_('initial_cost_name1'), db_column='initial_cost_name1', max_length=100, null=True, blank=True)
    initial_cost1 = models.IntegerField(_('initial_cost1'), db_column='initial_cost1', default=0)
    initial_cost_tax_type1 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id1',
        related_name='initial_cost_rooms1',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name2 = models.CharField(_('initial_cost_name2'), db_column='initial_cost_name2', max_length=100, null=True, blank=True)
    initial_cost2 = models.IntegerField(_('initial_cost2'), db_column='initial_cost2', default=0)
    initial_cost_tax_type2 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id2',
        related_name='initial_cost_rooms2',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name3 = models.CharField(_('initial_cost_name3'), db_column='initial_cost_name3', max_length=100, null=True, blank=True)
    initial_cost3 = models.IntegerField(_('initial_cost3'), db_column='initial_cost3', default=0)
    initial_cost_tax_type3 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id3',
        related_name='initial_cost_rooms3',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name4 = models.CharField(_('initial_cost_name4'), db_column='initial_cost_name4', max_length=100, null=True, blank=True)
    initial_cost4 = models.IntegerField(_('initial_cost4'), db_column='initial_cost4', default=0)
    initial_cost_tax_type4 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id4',
        related_name='initial_cost_rooms4',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name5 = models.CharField(_('initial_cost_name5'), db_column='initial_cost_name5', max_length=100, null=True, blank=True)
    initial_cost5 = models.IntegerField(_('initial_cost5'), db_column='initial_cost5', default=0)
    initial_cost_tax_type5 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id5',
        related_name='initial_cost_rooms5',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name6 = models.CharField(_('initial_cost_name6'), db_column='initial_cost_name6', max_length=100, null=True, blank=True)
    initial_cost6 = models.IntegerField(_('initial_cost6'), db_column='initial_cost6', default=0)
    initial_cost_tax_type6 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id6',
        related_name='initial_cost_rooms6',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name7 = models.CharField(_('initial_cost_name7'), db_column='initial_cost_name7', max_length=100, null=True, blank=True)
    initial_cost7 = models.IntegerField(_('initial_cost7'), db_column='initial_cost7', default=0)
    initial_cost_tax_type7 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id7',
        related_name='initial_cost_rooms7',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name8 = models.CharField(_('initial_cost_name8'), db_column='initial_cost_name8', max_length=100, null=True, blank=True)
    initial_cost8 = models.IntegerField(_('initial_cost8'), db_column='initial_cost8', default=0)
    initial_cost_tax_type8 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id8',
        related_name='initial_cost_rooms8',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name9 = models.CharField(_('initial_cost_name9'), db_column='initial_cost_name9', max_length=100, null=True, blank=True)
    initial_cost9 = models.IntegerField(_('initial_cost9'), db_column='initial_cost9', default=0)
    initial_cost_tax_type9 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id9',
        related_name='initial_cost_rooms9',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_name10 = models.CharField(_('initial_cost_name10'), db_column='initial_cost_name10', max_length=100, null=True, blank=True)
    initial_cost10 = models.IntegerField(_('initial_cost10'), db_column='initial_cost10', default=0)
    initial_cost_tax_type10 = models.ForeignKey(
        TaxType,
        db_column='initial_cost_tax_type_id10',
        related_name='initial_cost_rooms10',
        on_delete=models.PROTECT,
        default=0,
    )
    initial_cost_note = models.TextField(_('initial_cost_note'), db_column='initial_cost_note', max_length=2000, null=True, blank=True)

    free_rent_type = models.ForeignKey(
        FreeRentType,
        db_column='free_rent_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    free_rent_months = models.IntegerField(_('free_rent_months'), db_column='free_rent_months', default=0)
    free_rent_limit_year = models.IntegerField(_('free_rent_limit_year'), db_column='free_rent_limit_year', default=0)
    free_rent_limit_month = models.IntegerField(_('free_rent_limit_month'), db_column='free_rent_limit_month', default=0)
    cancel_notice_limit = models.IntegerField(_('cancel_notice_limit'), db_column='cancel_notice_limit', default=0)
    cancel_note = models.CharField(_('cancel_note'), db_column='cancel_note', max_length=255, null=True, blank=True)
    short_cancel_note = models.CharField(_('short_cancel_note'), db_column='short_cancel_note', max_length=255, null=True, blank=True)
    cleaning_type = models.ForeignKey(
        CleaningType,
        db_column='cleaning_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    cleaning_cost = models.IntegerField(_('cleaning_cost'), db_column='cleaning_cost', default=0)
    cleaning_cost_tax_type = models.ForeignKey(
        TaxType,
        db_column='cleaning_cost_tax_type_id',
        related_name='cleaning_cost_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    cleaning_note = models.CharField(_('cleaning_note'), db_column='cleaning_note', max_length=255, null=True, blank=True)

    electric_type = models.ForeignKey(
        ElectricType,
        db_column='electric_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    electric_comment = models.CharField(_('electric_comment'), db_column='electric_comment', max_length=100, null=True, blank=True)
    gas_type = models.ForeignKey(
        GasType,
        db_column='gas_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    gas_comment = models.CharField(_('gas_comment'), db_column='gas_comment', max_length=100, null=True, blank=True)
    bath_type = models.ForeignKey(
        BathType,
        db_column='bath_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    bath_comment = models.CharField(_('bath_comment'), db_column='bath_comment', max_length=100, null=True, blank=True)
    toilet_type = models.ForeignKey(
        ToiletType,
        db_column='toilet_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    toilet_comment = models.CharField(_('toilet_comment'), db_column='toilet_comment', max_length=100, null=True, blank=True)
    kitchen_range_type = models.ForeignKey(
        KitchenRangeType,
        db_column='kitchen_range_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    kitchen_range_comment = models.CharField(_('kitchen_range_comment'), db_column='kitchen_range_comment', max_length=100, null=True, blank=True)
    internet_type = models.ForeignKey(
        InternetType,
        db_column='internet_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    internet_comment = models.CharField(_('internet_comment'), db_column='internet_comment', max_length=100, null=True, blank=True)
    washer_type = models.ForeignKey(
        WasherType,
        db_column='washer_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    washer_comment = models.CharField(_('washer_comment'), db_column='washer_comment', max_length=100, null=True, blank=True)

    pet_type = models.ForeignKey(
        PetType,
        db_column='pet_type_id',
        related_name='rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    pet_comment = models.CharField(_('pet_comment'), db_column='pet_comment', max_length=100, null=True, blank=True)
    instrument_type = models.ForeignKey(
        AllowType,
        db_column='instrument_type_id',
        related_name='instrument_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    live_together_type = models.ForeignKey(
        AllowType,
        db_column='live_together_type_id',
        related_name='live_together_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    children_type = models.ForeignKey(
        AllowType,
        db_column='children_type_id',
        related_name='children_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    share_type = models.ForeignKey(
        AllowType,
        db_column='share_type_id',
        related_name='share_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    non_japanese_type = models.ForeignKey(
        AllowType,
        db_column='non_japanese_type_id',
        related_name='non_japanese_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    only_woman_type = models.ForeignKey(
        AllowType,
        db_column='only_woman_type_id',
        related_name='only_woman_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    only_man_type = models.ForeignKey(
        AllowType,
        db_column='only_man_type_id',
        related_name='only_man_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    corp_contract_type = models.ForeignKey(
        AllowType,
        db_column='corp_contract_type_id',
        related_name='corp_contract_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    student_type = models.ForeignKey(
        AllowType,
        db_column='student_type_id',
        related_name='student_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    new_student_type = models.ForeignKey(
        AllowType,
        db_column='new_student_type_id',
        related_name='new_student_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    welfare_type = models.ForeignKey(
        AllowType,
        db_column='welfare_type_id',
        related_name='welfare_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    office_use_type = models.ForeignKey(
        AllowType,
        db_column='office_use_type_id',
        related_name='office_use_rooms',
        on_delete=models.PROTECT,
        default=0,
    )
    constraint_note = models.CharField(_('constraint_note'), db_column='constraint_note', max_length=255, null=True, blank=True)

    reform_comment = models.CharField(_('reform_comment'), db_column='reform_comment', max_length=100, null=True, blank=True)
    reform_year = models.IntegerField(_('reform_year'), db_column='reform_year', default=0)
    reform_month = models.IntegerField(_('reform_month'), db_column='reform_month', default=0)
    reform_note = models.CharField(_('reform_note'), db_column='reform_note', max_length=255, null=True, blank=True)

    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'room'
        ordering = ['building_id', 'room_no', 'id']
        verbose_name = _('room')
        verbose_name_plural = _('rooms')

    def __str__(self):
        return self.room_no

    """
    プロパティ
    """
    @property
    def idb64(self):
        return base64_decode_id(self.pk)

    @property
    def building_oid(self):
        return self.building.oid

    @property
    def equipments(self):
        return self.room_equipments.filter(
            is_deleted=False,
            equipment__is_stopped=False,
        ).order_by('priority', 'equipment__category__priority', 'equipment__priority', 'id').all()

    @property
    def movies(self):
        return self.room_movies.filter(
            is_publish_vacancy=True,
            is_deleted=False,
        ).order_by('priority', 'movie_type__priority', 'id').all()

    @property
    def panoramas(self):
        return self.room_panoramas.filter(
            is_publish_vacancy=True,
            is_deleted=False,
        ).order_by('priority', 'panorama_type__priority', 'id').all()

    @property
    def pictures(self):
        return self.room_pictures.filter(
            is_publish_vacancy=True,
            is_deleted=False,
        ).order_by('priority', 'picture_type__priority').all()

    """
    表示用プロパティ
    """
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
    def payment_type_text(self):
        return DataHelper.get_payment_type_text(self.payment_type)

    @property
    def payment_fee_type_text(self):
        return DataHelper.get_payment_fee_type_text(self.payment_fee_type)

    @property
    def payment_fee_text(self):
        return DataHelper.get_payment_fee_text(
            self.payment_fee_type,
            self.payment_fee,
            self.payment_fee_tax_type)

    @property
    def free_rent_text(self):
        return DataHelper.get_free_rent_text(
            self.free_rent_type,
            self.free_rent_months,
            self.free_rent_limit_year,
            self.free_rent_limit_month)

    @property
    def monthly_cost_text1(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name1,
            self.monthly_cost1,
            self.monthly_cost_tax_type1)

    @property
    def monthly_cost_text2(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name2,
            self.monthly_cost2,
            self.monthly_cost_tax_type2)

    @property
    def monthly_cost_text3(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name3,
            self.monthly_cost3,
            self.monthly_cost_tax_type3)

    @property
    def monthly_cost_text4(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name4,
            self.monthly_cost4,
            self.monthly_cost_tax_type4)

    @property
    def monthly_cost_text5(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name5,
            self.monthly_cost5,
            self.monthly_cost_tax_type5)

    @property
    def monthly_cost_text6(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name6,
            self.monthly_cost6,
            self.monthly_cost_tax_type6)

    @property
    def monthly_cost_text7(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name7,
            self.monthly_cost7,
            self.monthly_cost_tax_type7)

    @property
    def monthly_cost_text8(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name8,
            self.monthly_cost8,
            self.monthly_cost_tax_type8)

    @property
    def monthly_cost_text9(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name9,
            self.monthly_cost9,
            self.monthly_cost_tax_type9)

    @property
    def monthly_cost_text10(self):
        return DataHelper.get_cost_text(
            self.monthly_cost_name10,
            self.monthly_cost10,
            self.monthly_cost_tax_type10)

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
    def insurance_company_text(self):
        return DataHelper.get_insurance_company_text(
            self.insurance_type,
            self.insurance_company)

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
    def document_cost_text(self):
        return DataHelper.get_existence_cost_text(
            self.document_cost_existence,
            self.document_cost,
            self.document_cost_tax_type)

    @property
    def key_change_cost_text(self):
        return DataHelper.get_existence_cost_text(
            self.key_change_cost_existence,
            self.key_change_cost,
            self.key_change_cost_tax_type)

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
    def initial_cost_text4(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name4,
            self.initial_cost4,
            self.initial_cost_tax_type4)

    @property
    def initial_cost_text5(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name5,
            self.initial_cost5,
            self.initial_cost_tax_type5)

    @property
    def initial_cost_text6(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name6,
            self.initial_cost6,
            self.initial_cost_tax_type6)

    @property
    def initial_cost_text7(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name7,
            self.initial_cost7,
            self.initial_cost_tax_type7)

    @property
    def initial_cost_text8(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name8,
            self.initial_cost8,
            self.initial_cost_tax_type8)

    @property
    def initial_cost_text9(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name9,
            self.initial_cost9,
            self.initial_cost_tax_type9)

    @property
    def initial_cost_text10(self):
        return DataHelper.get_cost_text(
            self.initial_cost_name10,
            self.initial_cost10,
            self.initial_cost_tax_type10)

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
    def renewal_charge_text(self):
        return DataHelper.get_existence_cost_text(
            self.renewal_charge_existence,
            self.renewal_charge,
            self.renewal_charge_tax_type)

    @property
    def recontract_fee_text(self):
        return DataHelper.get_existence_cost_text(
            self.recontract_fee_existence,
            self.recontract_fee,
            self.recontract_fee_tax_type)

    @property
    def cancel_notice_limit_text(self):
        return DataHelper.get_cancel_notice_limit_text(self.cancel_notice_limit)

    @property
    def cleaning_cost_text(self):
        return DataHelper.get_cleaning_cost_text(
            self.cleaning_type,
            self.cleaning_cost,
            self.cleaning_cost_tax_type)

    @property
    def room_area_text(self):
        return DataHelper.get_room_area_text(self.room_area)

    @property
    def balcony_type_text(self):
        return DataHelper.get_balcony_type_text(self.balcony_type)

    @property
    def balcony_area_text(self):
        return DataHelper.get_balcony_area_text(
            self.balcony_type,
            self.balcony_area)

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
    def live_start_date_text(self):
        ans = None
        if self.room_status.will_be_canceled:
            ans = DataHelper.get_date_string(
                self.live_start_year,
                self.live_start_month,
                self.live_start_day
            )

        return ans

    @property
    def cancel_scheduled_date_text(self):
        ans = None
        if self.room_status.will_be_canceled:
            ans = DataHelper.get_date_string(
                self.cancel_scheduled_year,
                self.cancel_scheduled_month,
                self.cancel_scheduled_day
            )

        return ans

    @property
    def reform_year_month(self):
        return DataHelper.get_reform_year_month(
            self.reform_year,
            self.reform_month)

    @property
    def electric_text(self):
        return DataHelper.get_electric_text(self.electric_type)

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
    def equipments_text(self):
        return DataHelper.get_equipments_text(self.equipments)

    @property
    def equipments_short_text(self):
        return DataHelper.get_equipments_short_text(self.equipments)

    @property
    def instrument_type_text(self):
        return DataHelper.get_allow_type_text(self.instrument_type)

    @property
    def live_together_type_text(self):
        return DataHelper.get_allow_type_text(self.live_together_type)

    @property
    def children_type_text(self):
        return DataHelper.get_allow_type_text(self.children_type)

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
    def corp_contract_type_text(self):
        return DataHelper.get_allow_type_text(self.corp_contract_type)

    @property
    def student_type_text(self):
        return DataHelper.get_allow_type_text(self.student_type)

    @property
    def new_student_type_text(self):
        return DataHelper.get_allow_type_text(self.new_student_type)

    @property
    def office_use_type_text(self):
        return DataHelper.get_allow_type_text(self.office_use_type)

    """
    空室条件取得用メソッド
    """
    @staticmethod
    def get_vacancy_room_condition(is_no_limit: bool, only_residential: bool, only_non_residential: bool):
        ans = Q(is_deleted=False, building__is_deleted=False)       # 削除されていない
        ans.add(Q(is_publish_web=True, building__is_hidden_web=False), Q.AND)   # WEB掲載の対象
        ans.add(Q(room_status__for_rent=True), Q.AND)  # 空き・空き予定

        if not is_no_limit:
            ans.add(
                Q(
                    Q(building__management_type__is_own=True)     # 自社物件
                    | Q(building__management_type__is_entrusted=True)  # 専任物件
                ) | Q(
                    building__management_type__is_condo_management=True,  # 分譲マンション
                    is_condo_management=True,  # 分譲管理の部屋
                ) | Q(is_sublease=True) | Q(is_entrusted=True),     # サブリース、専任の部屋
                Q.AND)

        if only_residential:
            ans.add(Q(rental_type__is_residential=True), Q.AND)
        elif only_non_residential:
            ans.add(Q(rental_type__is_non_residential=True), Q.AND)

        return ans
