"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import GarageType
import warnings


class GarageTypeModelTest(TestCase):
    """
    駐車場種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_is_paid(self):
        self.assertFalse(GarageType.objects.get(pk=0).is_paid)
        self.assertTrue(GarageType.objects.get(pk=1).is_paid)
        self.assertFalse(GarageType.objects.get(pk=2).is_paid)
        self.assertFalse(GarageType.objects.get(pk=3).is_paid)
        self.assertFalse(GarageType.objects.get(pk=4).is_paid)
        self.assertFalse(GarageType.objects.get(pk=5).is_paid)
