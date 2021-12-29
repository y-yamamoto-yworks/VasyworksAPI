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
from rent_db.models import Building
import warnings


class BuildingPictureModelTest(TestCase):
    """
    建物画像のテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.building = Building.objects.get(pk=2)      # 表示項目確認用マンション
        self.picture = self.building.building_pictures.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_building_picture_thumbnail_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'  # 表示項目確認用マンション
        cache_file_name = 'ae4499eed2c94f828cd0e37aec938558.JPG'  # 建物外観
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.picture.thumbnail_file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )

    def test_building_picture_small_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'  # 表示項目確認用マンション
        cache_file_name = '419e351b172545dbaffbd8932a172532.JPG'  # 建物外観
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.picture.small_file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )

    def test_building_picture_medium_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'  # 表示項目確認用マンション
        cache_file_name = '1dfebdf15b694cda969aecba97cf96f0.JPG'  # 建物外観
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.picture.medium_file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )

    def test_building_picture_large_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'  # 表示項目確認用マンション
        cache_file_name = 'd5f086f74ed749109bd04301078fce7b.JPG'  # 建物外観
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.picture.large_file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )
