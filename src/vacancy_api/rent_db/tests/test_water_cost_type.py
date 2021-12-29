"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import WaterCostType
import warnings


class WaterCostTypeModelTest(TestCase):
    """
    水道費種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_is_money(self):
        self.assertFalse(WaterCostType.objects.get(pk=0).is_money)
        self.assertFalse(WaterCostType.objects.get(pk=10).is_money)
        self.assertTrue(WaterCostType.objects.get(pk=20).is_money)
        self.assertFalse(WaterCostType.objects.get(pk=30).is_money)
        self.assertFalse(WaterCostType.objects.get(pk=31).is_money)
