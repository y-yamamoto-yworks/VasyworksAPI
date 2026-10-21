"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
import os
import re
import sys
import shutil
from django.conf import settings
from django.core.exceptions import SuspiciousFileOperation
from urllib.parse import urljoin
from lib.image_helper import ImageHelper


class CacheFileHelper:
    """キャッシュファイルヘルパークラス"""
    @staticmethod
    def _get_safe_path(base_dir, *paths):
        real_base = os.path.realpath(base_dir)
        target_path = os.path.realpath(os.path.join(real_base, *paths))

        if os.path.commonpath([real_base, target_path]) != real_base:
            raise SuspiciousFileOperation("Invalid file path (Path Traversal detected).")

        return target_path

    @staticmethod
    def __prepare_cache_dir():
        """ キャッシュ用ディレクトリの準備"""
        cache_path = CacheFileHelper._get_safe_path(settings.CACHE_FILE_DIR, "buildings")
        if not os.path.isdir(cache_path):
            os.makedirs(cache_path)

        cache_path = CacheFileHelper._get_safe_path(settings.CACHE_FILE_DIR, "documents")
        if not os.path.isdir(cache_path):
            os.makedirs(cache_path)

    @staticmethod
    def __copy_file(src, dest):
        """ファイルのコピー"""
        ans = False
        secure_src = CacheFileHelper._get_safe_path(settings.ORIGINAL_FILE_DIR, src)
        secure_dest = CacheFileHelper._get_safe_path(settings.CACHE_FILE_DIR, dest)

        if os.path.exists(secure_src) and not os.path.exists(secure_dest):
            try:
                shutil.copy2(secure_src, secure_dest)
                ans = True
            except:
                ans = False

        return ans

    @staticmethod
    def __get_property_file_url(file_oid, file_dir, org_file_name, cache_file_name):
        """ 建物、部屋のファイルのURLの取得（画像ファイル以外） """
        safe_oid = os.path.basename(str(file_oid))
        safe_dir = os.path.basename(str(file_dir))
        safe_org_name = os.path.basename(str(org_file_name))
        safe_cache_name = os.path.basename(str(cache_file_name))

        CacheFileHelper.__prepare_cache_dir()
        cache_path = CacheFileHelper._get_safe_path(settings.CACHE_FILE_DIR, 'buildings', safe_oid)
        cache_url = urljoin(settings.CACHE_FILE_URL, "./buildings/" + safe_oid + "/")
        if not os.path.isdir(cache_path):
            os.makedirs(cache_path)

        cache_file_url = None
        org_file_path = CacheFileHelper._get_safe_path(
            settings.ORIGINAL_FILE_DIR, 'buildings', safe_oid, safe_dir, safe_org_name
        )
        if os.path.isfile(org_file_path):
            cache_file_path = CacheFileHelper._get_safe_path(cache_path, safe_cache_name)
            cache_file_url = urljoin(cache_url, safe_cache_name)
            if not os.path.isfile(cache_file_path):
                CacheFileHelper.__copy_file(org_file_path, cache_file_path)

        return urljoin(settings.BASE_URL, cache_file_url)

    @staticmethod
    def get_property_image_file_url(file_oid, org_file_name, cache_file_name, water_mark, max_size):
        """ 建物、部屋の画像のURLの取得 """
        safe_oid = os.path.basename(str(file_oid))
        safe_org_name = os.path.basename(str(org_file_name))
        safe_cache_name = os.path.basename(str(cache_file_name))

        CacheFileHelper.__prepare_cache_dir()
        cache_path = CacheFileHelper._get_safe_path(settings.CACHE_FILE_DIR, 'buildings', safe_oid)
        cache_url = urljoin(settings.CACHE_FILE_URL, "./buildings/" + safe_oid + "/")
        if not os.path.isdir(cache_path):
            os.makedirs(cache_path)

        cache_file_url = None
        org_file_path = CacheFileHelper._get_safe_path(
            settings.ORIGINAL_FILE_DIR, 'buildings', safe_oid, 'pictures', safe_org_name
        )
        if os.path.isfile(org_file_path):
            cache_file_path = CacheFileHelper._get_safe_path(cache_path, safe_cache_name)
            cache_file_url = urljoin(cache_url, safe_cache_name)
            if not os.path.isfile(cache_file_path):
                ImageHelper.cache_image(org_file_path, cache_file_path, water_mark, max_size)

        return urljoin(settings.BASE_URL, cache_file_url)

    @staticmethod
    def get_property_panorama_file_url(file_oid, org_file_name, cache_file_name):
        """建物、部屋のパノラマのURL取得"""
        return CacheFileHelper.__get_property_file_url(file_oid, 'panoramas', org_file_name, cache_file_name)

    @staticmethod
    def get_property_movie_file_url(file_oid, org_file_name, cache_file_name):
        """建物、部屋の動画のURL取得"""
        return CacheFileHelper.__get_property_file_url(file_oid, 'movies', org_file_name, cache_file_name)

    @staticmethod
    def get_building_file_url(file_oid, org_file_name, cache_file_name):
        """建物ファイルのURL取得"""
        return CacheFileHelper.__get_property_file_url(file_oid, 'files', org_file_name, cache_file_name)

    @staticmethod
    def get_document_file_url(org_file_name, cache_file_name):
        """書類ファイルのURL取得"""
        safe_org_name = os.path.basename(str(org_file_name))
        safe_cache_name = os.path.basename(str(cache_file_name))

        CacheFileHelper.__prepare_cache_dir()
        cache_path = CacheFileHelper._get_safe_path(settings.CACHE_FILE_DIR, 'documents')
        cache_url = urljoin(settings.CACHE_FILE_URL, "./documents/")

        cache_file_url = None
        org_file_path = CacheFileHelper._get_safe_path(
            settings.ORIGINAL_FILE_DIR, 'documents', 'files', safe_org_name
        )
        if os.path.isfile(org_file_path):
            cache_file_path = CacheFileHelper._get_safe_path(cache_path, safe_cache_name)
            cache_file_url = urljoin(cache_url, safe_cache_name)
            if not os.path.isfile(cache_file_path):
                CacheFileHelper.__copy_file(org_file_path, cache_file_path)

        return urljoin(settings.BASE_URL, cache_file_url)
