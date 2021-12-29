"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from unittest import TestCase
from django.conf import settings
from urllib.parse import urljoin
from django.db import transaction
from rent_db.models import Room
import warnings


class RoomPictureModelTest(TestCase):
    """
    部屋画像のテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.room = Room.objects.get(pk=3)      # 表示項目確認用マンション DEMO1号室
        self.picture = self.room.room_pictures.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_building_picture_thumbnail_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'  # 表示項目確認用マンション
        cache_file_name = '900b32b744674f82b4fe2a26ea81377e.jpg'  # 間取図
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.picture.thumbnail_file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )

    def test_building_picture_small_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'  # 表示項目確認用マンション
        cache_file_name = 'cdd14c95424748bcb3edc0046e3cc264.jpg'  # 間取図
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.picture.small_file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )

    def test_building_picture_medium_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'  # 表示項目確認用マンション
        cache_file_name = 'bfd69456861e4c23b90518cb3b243e88.jpg'  # 間取図
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.picture.medium_file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )

    def test_building_picture_large_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'  # 表示項目確認用マンション
        cache_file_name = 'b75ea07ff27241f28b33a6f4c5d48395.jpg'  # 間取図
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.picture.large_file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )
