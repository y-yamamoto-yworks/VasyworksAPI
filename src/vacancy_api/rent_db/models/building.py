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
from .area import Area
from .arrival_type import ArrivalType
from .bike_parking_type import BikeParkingType
from .building_garage import BuildingGarage
from .building_type import BuildingType
from .city import City
from .department import Department
from .elementary_school import ElementarySchool
from .existence import Existence
from .garage_type import GarageType
from .garage_status import GarageStatus
from .junior_high_school import JuniorHighSchool
from .management_type import ManagementType
from .pref import Pref
from .room import Room
from .staff import Staff
from .station import Station
from .structure import Structure
from .tax_type import TaxType
from users.models import VacancyUser


class Building(models.Model):
    """
    建物
    """
    is_no_limit = False         # 自社物件以外も含む場合はTrue
    is_only_residential = False      # 居住用のみ対象の場合はTrue
    is_only_non_residential = False  # 非居住用のみ対象の場合はTrue

    id = models.AutoField(_('id'), db_column='id', primary_key=True)

    oid = models.CharField(_('oid'), db_column='oid', db_index=True, unique=True, max_length=50)
    file_oid = models.CharField(_('file_oid'), db_column='file_oid', db_index=True, unique=True, max_length=50)
    building_code = models.CharField(_('building_code'), db_column='building_code', max_length=20, db_index=True, null=True, blank=True)
    building_name = models.CharField(_('building_name'), db_column='building_name', max_length=100, db_index=True, null=True, blank=True)
    building_kana = models.CharField(_('building_kana'), db_column='building_kana', max_length=100, db_index=True, null=True, blank=True)
    building_old_name = models.CharField(_('building_old_name'), db_column='building_old_name', max_length=100, null=True, blank=True)

    postal_code = models.CharField(_('postal_code'), db_column='postal_code', max_length=10, null=True, blank=True)
    pref = models.ForeignKey(
        Pref,
        db_column='pref_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_trading_area=True) | Q(pk=0),
    )
    city = models.ForeignKey(
        City,
        db_column='city_id',
        related_name='buildings',
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
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False) | Q(pk=0),
    )

    elementary_school = models.ForeignKey(
        ElementarySchool,
        db_column='elementary_school_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False) | Q(pk=0),
    )
    elementary_school_distance = models.IntegerField(_('elementary_school_distance'), db_column='elementary_school_distance', default=0)

    junior_high_school = models.ForeignKey(
        JuniorHighSchool,
        db_column='junior_high_school_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False) | Q(pk=0),
    )
    junior_high_school_distance = models.IntegerField(_('junior_high_school_distance'), db_column='junior_high_school_distance', default=0)
    around_note = models.CharField(_('around_note'), db_column='around_note', max_length=255, null=True, blank=True)

    management_type = models.ForeignKey(
        ManagementType,
        db_column='management_type_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    department = models.ForeignKey(
        Department,
        db_column='department_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    staff1 = models.ForeignKey(
        Staff,
        db_column='staff_id1',
        related_name='staff1_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    staff2 = models.ForeignKey(
        Staff,
        db_column='staff_id2',
        related_name='staff2_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )
    priority_level = models.IntegerField(_('priority_level'), db_column='priority_level', db_index=True, default=50)
    agency_department = models.ForeignKey(
        Department,
        db_column='agency_department_id',
        related_name='agency_buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
        limit_choices_to=Q(is_stopped=False, is_deleted=False) | Q(pk=0),
    )

    arrival_type1 = models.ForeignKey(
        ArrivalType,
        db_column='arrival_type_id1',
        related_name='buildings1',
        on_delete=models.PROTECT,
        default=0,
    )
    station1 = models.ForeignKey(
        Station,
        db_column='station_id1',
        related_name='buildings1',
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
        related_name='buildings2',
        on_delete=models.PROTECT,
        default=0,
    )
    station2 = models.ForeignKey(
        Station,
        db_column='station_id2',
        related_name='buildings2',
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
        related_name='buildings3',
        on_delete=models.PROTECT,
        default=0,
    )
    station3 = models.ForeignKey(
        Station,
        db_column='station_id3',
        related_name='buildings3',
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
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    building_type_comment = models.CharField(_('building_type_comment'), db_column='building_type_comment', max_length=100, null=True, blank=True)
    structure = models.ForeignKey(
        Structure,
        db_column='structure_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    structure_comment = models.CharField(_('structure_comment'), db_column='structure_comment', max_length=100, null=True, blank=True)
    building_rooms = models.IntegerField(_('building_rooms'), db_column='building_rooms', default=0)
    building_floors = models.IntegerField(_('building_floors'), db_column='building_floors', default=0)
    building_undergrounds = models.IntegerField(_('building_undergrounds'), db_column='building_undergrounds', default=0)
    build_year = models.IntegerField(_('build_year'), db_column='build_year', db_index=True, default=1970)
    build_month = models.IntegerField(_('build_month'), db_column='build_month', default=1)

    bike_parking_type = models.ForeignKey(
        BikeParkingType,
        db_column='bike_parking_type_id',
        related_name='buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    with_bike_parking_roof = models.BooleanField(_('with_bike_parking_roof'), db_column='with_bike_parking_roof', default=False)
    bike_parking_fee_lower = models.IntegerField(_('bike_parking_fee_lower'), db_column='bike_parking_fee_lower', default=0)
    bike_parking_fee_upper = models.IntegerField(_('bike_parking_fee_upper'), db_column='bike_parking_fee_upper', default=0)
    bike_parking_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='bike_parking_fee_tax_type_id',
        related_name='bike_parking_fee_buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    bike_parking_note = models.CharField(_('bike_parking_note'), db_column='bike_parking_note', max_length=255, null=True, blank=True)
    garage_type = models.ForeignKey(
        GarageType,
        db_column='garage_type_id',
        related_name='buildings',
        db_index=True,
        on_delete=models.PROTECT,
        default=0,
    )
    garage_status = models.ForeignKey(
        GarageStatus,
        db_column='garage_status_id',
        related_name='buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_distance = models.IntegerField(_('garage_distance'), db_column='garage_distance', default=0)
    garage_fee_lower = models.IntegerField(_('garage_fee_lower'), db_column='garage_fee_lower', default=0)
    garage_fee_upper = models.IntegerField(_('garage_fee_upper'), db_column='garage_fee_upper', default=0)
    garage_fee_tax_type = models.ForeignKey(
        TaxType,
        db_column='garage_fee_tax_type_id',
        related_name='garage_fee_buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_charge_lower = models.IntegerField(_('garage_charge_lower'), db_column='garage_charge_lower', default=0)
    garage_charge_upper = models.IntegerField(_('garage_charge_upper'), db_column='garage_charge_upper', default=0)
    garage_charge_tax_type = models.ForeignKey(
        TaxType,
        db_column='garage_charge_tax_type_id',
        related_name='garage_charge_buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    garage_note = models.CharField(_('garage_note'), db_column='garage_note', max_length=255, null=True, blank=True)
    building_management_company = models.CharField(_('building_management_company'), db_column='building_management_company', max_length=100, null=True, blank=True)
    building_management_address = models.CharField(_('building_management_address'), db_column='building_management_address', max_length=255, null=True, blank=True)
    building_management_tel = models.CharField(_('building_management_tel'), db_column='building_management_tel', max_length=20, null=True, blank=True)
    building_management_no = models.CharField(_('building_management_no'), db_column='building_management_no', max_length=50, null=True, blank=True)
    building_management_note = models.CharField(_('building_management_note'), db_column='building_management_note', max_length=255, null=True, blank=True)

    agreement_existence = models.ForeignKey(
        Existence,
        db_column='agreement_existence_id',
        related_name='agreement_existence_buildings',
        on_delete=models.PROTECT,
        default=0,
    )
    apartment_manager_comment = models.CharField(_('apartment_manager_comment'), db_column='apartment_manager_comment', max_length=100, null=True, blank=True)

    auto_lock_no = models.CharField(_('auto_lock_no'), db_column='auto_lock_no', max_length=20, null=True, blank=True)

    is_hidden_web = models.BooleanField(_('is_hidden_web'), db_column='is_hidden_web', db_index=True, default=False)
    web_catch_copy = models.CharField(_('web_catch_copy'), db_column='web_catch_copy', max_length=100, null=True, blank=True)
    web_appeal = models.CharField(_('web_appeal'), db_column='web_appeal', max_length=255, null=True, blank=True)
    web_note = models.TextField(_('web_note'), db_column='web_note', max_length=2000, null=True, blank=True)

    tenant_note = models.TextField(_('tenant_note'), db_column='tenant_note', max_length=2000, null=True, blank=True)
    garbage_note = models.TextField(_('garbage_note'), db_column='garbage_note', max_length=2000, null=True, blank=True)
    private_note = models.TextField(_('private_note'), db_column='private_note', max_length=2000, null=True, blank=True)
    management_note = models.TextField(_('management_note'), db_column='management_note', max_length=2000, null=True, blank=True)

    is_deleted = models.BooleanField(_('is_deleted'), db_column='is_deleted', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'building'
        ordering = ['building_kana', 'id']
        verbose_name = _('building')
        verbose_name_plural = _('buildings')

    def __str__(self):
        return self.building_name

    """
    プロパティ
    """
    @property
    def idb64(self):
        return base64_decode_id(self.pk)

    @property
    def building_id_text(self):
        ans = '{:0>6}'.format(self.id)
        if self.building_code:
            ans = self.building_code

        return ans

    @property
    def vacancy_rooms(self):
        return self.rooms.filter(
            Room.get_vacancy_room_condition(
                self.is_no_limit,
                self.is_only_residential,
                self.is_only_non_residential,
            )
        ).order_by('room_no', 'id').all()

    @property
    def facilities(self):
        return self.building_facilities.filter(
            is_deleted=False,
        ).order_by('priority', 'facility__priority', 'id').all()

    @property
    def garages(self):
        return self.building_garages.filter(
            garage_status__id__in=[1, 3, 4],
            is_deleted=False,
        ).order_by('priority', 'garage_name', 'id').all()

    @property
    def landmarks(self):
        return self.building_landmarks.filter(
            is_deleted=False,
        ).order_by('priority', 'landmark__priority', 'id').all()

    @property
    def files(self):
        return self.building_files.filter(
            is_publish_web=True,
            is_deleted=False,
        ).order_by('priority', 'id').all()

    @property
    def movies(self):
        return self.building_movies.filter(
            is_publish_web=True,
            is_deleted=False,
        ).order_by('priority', 'movie_type__priority', 'id').all()

    @property
    def panoramas(self):
        return self.building_panoramas.filter(
            is_publish_web=True,
            is_deleted=False,
        ).order_by('priority', 'panorama_type__priority', 'id').all()

    @property
    def pictures(self):
        return self.building_pictures.filter(
            is_publish_web=True,
            is_deleted=False,
        ).order_by('priority', 'picture_type__priority', 'id').all()

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
            self.building_type,
            self.building_type_comment)

    @property
    def build_year_month(self):
        return DataHelper.get_build_year_month_text(
            self.build_year,
            self.build_month)

    @property
    def structure_text(self):
        return DataHelper.get_structure_text(
            self.structure,
            self.structure_comment)

    @property
    def elementary_school_text(self):
        return DataHelper.get_school_text(self.elementary_school)

    @property
    def elementary_school_distance_text(self):
        return DataHelper.get_school_distance_text(
            self.elementary_school,
            self.elementary_school_distance)

    @property
    def junior_high_school_text(self):
        return DataHelper.get_school_text(self.junior_high_school)

    @property
    def junior_high_school_distance_text(self):
        return DataHelper.get_school_distance_text(
            self.junior_high_school,
            self.junior_high_school_distance)

    @property
    def garage_type_text(self):
        return DataHelper.get_garage_type_text(self.garage_type)

    @property
    def garage_status_text(self):
        return DataHelper.get_building_garage_status_text(
            self.garage_type,
            self.garage_status)

    @property
    def garage_distance_text(self):
        return DataHelper.get_building_garage_distance_text(
            self.garage_type,
            self.garage_distance)

    @property
    def garage_fee_text(self):
        return DataHelper.get_building_garage_fee_text(
            self.garage_type,
            self.garage_fee_lower,
            self.garage_fee_upper,
            self.garage_fee_tax_type)

    @property
    def garage_charge_text(self):
        return DataHelper.get_building_garage_charge_text(
            self.garage_charge_lower,
            self.garage_charge_upper,
            self.garage_charge_tax_type)

    @property
    def bike_parking_type_text(self):
        return DataHelper.get_bike_parking_type_text(self.bike_parking_type)

    @property
    def bike_parking_roof_text(self):
        return DataHelper.get_bike_parking_roof_text(
            self.bike_parking_type,
            self.with_bike_parking_roof)

    @property
    def bike_parking_fee_text(self):
        return DataHelper.get_bike_parking_fee_text(
            self.bike_parking_type,
            self.bike_parking_fee_lower,
            self.bike_parking_fee_upper,
            self.bike_parking_fee_tax_type)

    @property
    def staff1_text(self):
        return DataHelper.get_staff_text(self.staff1)

    @property
    def staff2_text(self):
        return DataHelper.get_staff_text(self.staff2)

    @property
    def agreement_existence_text(self):
        return DataHelper.get_is_exist_text(self.agreement_existence)
