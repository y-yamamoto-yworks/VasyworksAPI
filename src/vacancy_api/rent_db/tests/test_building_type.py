"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.db import transaction
from rent_db.models import BuildingType
import warnings


class BuildingTypeModelTest(TestCase):
    """
    建物種別モデルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_is_condominium(self):
        self.assertFalse(BuildingType.objects.get(pk=0).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=10).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=20).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=30).is_condominium)
        self.assertTrue(BuildingType.objects.get(pk=40).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=50).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=51).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=90).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=110).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=120).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=130).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=140).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=210).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=220).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=310).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=320).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=330).is_condominium)
        self.assertFalse(BuildingType.objects.get(pk=990).is_condominium)
