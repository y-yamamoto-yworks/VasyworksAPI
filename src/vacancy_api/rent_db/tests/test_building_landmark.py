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


class BuildingLandmarkModelTest(TestCase):
    """
    建物ランドマークのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.building = Building.objects.get(pk=2)      # 表示項目確認用マンション
        self.landmark = self.building.building_landmarks.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def test_building_oid(self):
        self.assertEqual(self.landmark.building_oid, '98d6c2ccd9384062ab5fb4dd61b3e8fc')

    def test_building_facility_distance_text(self):
        self.assertEqual(self.landmark.distance_text, '100m')
