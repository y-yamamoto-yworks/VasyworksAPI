"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lib.convert import *
from lib.functions import *
from .area import Area
from .elementary_school import ElementarySchool
from .junior_high_school import JuniorHighSchool
from .pref import Pref


class City(models.Model):
    """
    市区町村
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)
    name = models.CharField(_('name'), db_column='name', max_length=50)

    pref = models.ForeignKey(
        Pref,
        db_column='pref_id',
        related_name='pref_cites',
        db_index=True,
        on_delete=models.PROTECT,
    )

    priority = models.IntegerField(_('priority'), db_column='priority', db_index=True, default=100)
    lat = models.FloatField(_('lat'), db_column='lat', db_index=True, default=0)
    lng = models.FloatField(_('lng'), db_column='lng', db_index=True, default=0)
    is_trading_area = models.BooleanField(_('is_trading_area'), db_column='is_trading_area', db_index=True, default=False)
    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    areas = models.ManyToManyField(
        Area,
        related_name='city_area_cities',
        through='CityArea',
    )

    elementary_schools = models.ManyToManyField(
        ElementarySchool,
        related_name='city_elementary_school_cities',
        through='CityElementarySchool',
    )

    junior_high_schools = models.ManyToManyField(
        JuniorHighSchool,
        related_name='city_junior_high_school_cities',
        through='CityJuniorHighSchool',
    )

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'city'
        ordering = ['pref_id', 'priority', 'id']
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    @property
    def idb64(self):
        return base64_decode_id(self.pk)

    @property
    def related_areas(self):
        ans = self.areas.filter(
            is_stopped=False,
        ).order_by('kana').all()

        return ans

    @property
    def related_elementary_schools(self):
        ans = self.elementary_schools.filter(
            is_stopped=False,
        ).order_by('kana').all()

        return ans

    @property
    def related_junior_high_schools(self):
        ans = self.junior_high_schools.filter(
            is_stopped=False,
        ).order_by('kana').all()

        return ans


class CityArea(models.Model):
    """
    市区町村エリア
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)

    city = models.ForeignKey(
        'City',
        db_column='city_id',
        related_name='city_areas',
        db_index=True,
        on_delete=models.PROTECT,
    )

    area = models.ForeignKey(
        Area,
        db_column='area_id',
        related_name='area_cities',
        on_delete=models.PROTECT,
    )

    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'city_area'
        ordering = ['city_id', 'area_id', 'id']
        verbose_name = _('city_area')
        verbose_name_plural = _('city_areas')


class CityElementarySchool(models.Model):
    """
    市区町村小学校区
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)

    city = models.ForeignKey(
        'City',
        db_column='city_id',
        related_name='city_elementary_schools',
        db_index=True,
        on_delete=models.PROTECT,
    )

    school = models.ForeignKey(
        ElementarySchool,
        db_column='school_id',
        related_name='school_cities',
        on_delete=models.PROTECT,
    )

    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'city_elementary_school'
        ordering = ['city_id', 'school_id', 'id']
        verbose_name = _('city_elementary_school')
        verbose_name_plural = _('city_elementary_schools')


class CityJuniorHighSchool(models.Model):
    """
    市区町村中学校区
    """
    id = models.IntegerField(_('id'), db_column='id', primary_key=True)

    city = models.ForeignKey(
        'City',
        db_column='city_id',
        related_name='city_junior_high_schools',
        db_index=True,
        on_delete=models.PROTECT,
    )

    school = models.ForeignKey(
        JuniorHighSchool,
        db_column='school_id',
        related_name='school_cities',
        on_delete=models.PROTECT,
    )

    is_stopped = models.BooleanField(_('is_stopped'), db_column='is_stopped', db_index=True, default=False)

    class Meta:
        managed = False
        db_table = 'city_junior_high_school'
        ordering = ['city_id', 'school_id', 'id']
        verbose_name = _('city_junior_high_school')
        verbose_name_plural = _('city_junior_high_schools')
