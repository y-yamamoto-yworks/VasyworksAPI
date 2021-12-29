"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import City
import warnings


class CityModelTest(TestCase):
    """
    市区町村モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_related_areas(self):
        city = City.objects.get(pk=26101)       # 京都市北区
        area = city.related_areas.first()       # 大北山
        self.assertEqual(area.name, '大北山')

    def test_related_elementary_schools(self):
        city = City.objects.get(pk=26101)       # 京都市北区
        school = city.related_elementary_schools.first()       # 大宮
        self.assertEqual(school.name, '大宮')

    def test_related_junior_high_schools(self):
        city = City.objects.get(pk=26101)       # 京都市北区
        school = city.related_junior_high_schools.first()       # 旭丘
        self.assertEqual(school.name, '旭丘')
