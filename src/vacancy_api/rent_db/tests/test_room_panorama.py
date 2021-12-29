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


class RoomPanoramaModelTest(TestCase):
    """
    部屋パノラマのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.room = Room.objects.get(pk=3)      # 表示項目確認用マンション DEMO1号室
        self.panorama = self.room.room_panoramas.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_room_panorama_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'   # 表示項目確認用マンション
        cache_file_name = '8445bbd9566443f0b5543ba443cdfe6e.JPG'      # 居室（洋室）
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.panorama.file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )
