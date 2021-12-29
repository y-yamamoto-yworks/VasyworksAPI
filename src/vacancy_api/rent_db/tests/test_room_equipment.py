"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import Room
import warnings


class RoomEquipmentModelTest(TestCase):
    """
    部屋設備のテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.room = Room.objects.get(pk=3)      # 表示項目確認用マンション DEMO1号室
        self.equipment = self.room.equipments.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_building_oid(self):
        self.assertEqual(self.equipment.building_oid, '98d6c2ccd9384062ab5fb4dd61b3e8fc')

    def test_room_oid(self):
        self.assertEqual(self.equipment.room_oid, '5073ab83b3204160a947d1ab470a0b2b')
