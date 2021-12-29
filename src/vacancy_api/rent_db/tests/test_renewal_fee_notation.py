"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import RenewalFeeNotation
import warnings


class RenewalFeeNotationModelTest(TestCase):
    """
    更新料表記モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_is_money(self):
        self.assertFalse(RenewalFeeNotation.objects.get(pk=0).is_money)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=1).is_money)
        self.assertTrue(RenewalFeeNotation.objects.get(pk=2).is_money)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=3).is_money)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=4).is_money)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=5).is_money)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=6).is_money)

    def test_is_month(self):
        self.assertFalse(RenewalFeeNotation.objects.get(pk=0).is_month)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=1).is_month)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=2).is_month)
        self.assertTrue(RenewalFeeNotation.objects.get(pk=3).is_month)
        self.assertTrue(RenewalFeeNotation.objects.get(pk=4).is_month)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=5).is_month)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=6).is_month)

    def test_is_rate(self):
        self.assertFalse(RenewalFeeNotation.objects.get(pk=0).is_rate)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=1).is_rate)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=2).is_rate)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=3).is_rate)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=4).is_rate)
        self.assertTrue(RenewalFeeNotation.objects.get(pk=5).is_rate)
        self.assertFalse(RenewalFeeNotation.objects.get(pk=6).is_rate)
