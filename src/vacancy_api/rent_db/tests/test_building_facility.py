"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import Building
import warnings


class BuildingFacilityModelTest(TestCase):
    """
    建物周辺施設のテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.building = Building.objects.get(pk=2)      # 表示項目確認用マンション
        self.facility = self.building.building_facilities.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_building_oid(self):
        self.assertEqual(self.facility.building_oid, '98d6c2ccd9384062ab5fb4dd61b3e8fc')

    def test_building_facility_distance_text(self):
        self.assertEqual(self.facility.distance_text, '100m')
