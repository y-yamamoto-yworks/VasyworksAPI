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


class BuildingMovieModelTest(TestCase):
    """
    建物動画のテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')
        self.building = Building.objects.get(pk=2)      # 表示項目確認用マンション
        self.movie = self.building.building_movies.first()

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_building_oid(self):
        self.assertEqual(self.movie.building_oid, '98d6c2ccd9384062ab5fb4dd61b3e8fc')

    def test_building_movie_file_url(self):
        file_oid = '7112299ba5e743428e02a0824a3582d0'   # 表示項目確認用マンション
        cache_file_name = '1bae955702b9426a8a0cb73152c7abe2.mp4'      # 屋内スペース
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            self.movie.file_url,
            urljoin(cache_file_url, "./buildings/" + file_oid + "/" + cache_file_name),
        )
