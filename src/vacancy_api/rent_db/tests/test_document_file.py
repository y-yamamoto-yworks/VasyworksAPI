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
from rent_db.models import DocumentFile
import warnings


class DocumentFileModelTest(TestCase):
    """
    書類ファイルのテスト
    """
    def setUp(self):
        warnings.simplefilter('ignore')

        if transaction.get_autocommit():
            transaction.set_autocommit(False)

    def tearDown(self):
        transaction.rollback()

    def test_document_file_cache_file_url(self):
        file = DocumentFile.objects.get(pk=1)       # 書類サンプル1
        cache_file_name = '5b32df9306ae464ba5fd1ccace463ee3.pdf'      # 書類サンプル1
        cache_file_url = urljoin(settings.BASE_URL, settings.CACHE_FILE_URL)
        self.assertEqual(
            file.file_url,
            urljoin(cache_file_url, "./documents/" + cache_file_name),
        )
