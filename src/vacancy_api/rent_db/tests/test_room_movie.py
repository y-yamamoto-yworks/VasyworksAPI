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


class RoomMovieModelTest(TestCase):
    """
    部屋動画のテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.room = Room.objects.get(pk=3)      # 表示項目確認用マンション DEMO1号室
        self.movie = self.room.room_movies.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_room_movie_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'   # 表示項目確認用マンション
        cache_file_name = '240a825cd2c54494a830c188e1c6b8af.mp4'      # 室内
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.movie.file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )
