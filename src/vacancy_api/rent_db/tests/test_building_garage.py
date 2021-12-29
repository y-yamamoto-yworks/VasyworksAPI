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


class BuildingGarageModelTest(TestCase):
    """
    建物駐車場モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.building = Building.objects.get(pk=2)      # 表示項目確認用マンション
        self.garage = self.building.building_garages.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_building_oid(self):
        self.assertEqual(self.garage.building_oid, '98d6c2ccd9384062ab5fb4dd61b3e8fc')

    def test_building_garage_garage_status_text(self):
        self.assertEqual(self.garage.garage_status_text, '空き有')

    def test_building_garage_garage_fee_text(self):
        self.assertEqual(self.garage.garage_fee_text, '10,000円（税別）')
        self.garage.garage_fee = 0
        self.assertIsNone(self.garage.garage_fee_text)

    def test_building_garage_garage_charge_text(self):
        self.assertEqual(self.garage.garage_charge_text, '5,000円（税別）')
        self.garage.garage_charge = 0
        self.assertIsNone(self.garage.garage_charge_text)

    def test_building_garage_garage_deposit_text(self):
        self.assertEqual(self.garage.garage_deposit_text, '10,000円（税別）')
        self.garage.garage_deposit = 0
        self.assertIsNone(self.garage.garage_deposit_text)

    def test_building_garage_certification_fee_text(self):
        self.assertEqual(self.garage.certification_fee_text, '6,000円（税別）')
        self.garage.certification_fee = 0
        self.assertIsNone(self.garage.certification_fee_text)

    def test_building_garage_initial_cost_text1(self):
        self.assertEqual(self.garage.initial_cost_text1, '3,000円(税込)')

    def test_building_garage_initial_cost_text2(self):
        self.assertEqual(self.garage.initial_cost_text2, '5,000円(税込)')

    def test_building_garage_initial_cost_text3(self):
        self.assertEqual(self.garage.initial_cost_text3, '1,000円(税込)')

    def test_building_garage_allow_no_room_text(self):
        self.assertIsNone(self.garage.allow_no_room_text)
        old_allow_no_room = self.garage.allow_no_room
        self.garage.allow_no_room = True
        self.assertEqual(self.garage.allow_no_room_text, '外部貸し可')
        self.garage.allow_no_room = old_allow_no_room

    def test_building_garage_garage_size_text(self):
        self.assertEqual(self.garage.garage_size_text, '幅1.5m×奥行5m×高さ3m')
