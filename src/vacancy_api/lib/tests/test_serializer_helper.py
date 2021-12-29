"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
from urllib.parse import urljoin
import warnings
import os
from lib.serializer_helper import SerializerHelper


class SerializerHelperTest(TestCase):
    """
    シリアライザ用のヘルパークラスのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

    def test_get_building_picture_fields(self):
        self.assertEqual(
            SerializerHelper.get_building_picture_fields(),
            (
                'id',
                'idb64',
                'building_oid',
                'picture_type',
                'thumbnail_file_url',
                'small_file_url',
                'medium_file_url',
                'large_file_url',
                'comment',
            )
        )

    def test_get_room_picture_fields(self):
        self.assertEqual(
            SerializerHelper.get_room_picture_fields(),
            (
                'id',
                'idb64',
                'building_oid',
                'room_oid',
                'picture_type',
                'thumbnail_file_url',
                'small_file_url',
                'medium_file_url',
                'large_file_url',
                'comment',
            )
        )
