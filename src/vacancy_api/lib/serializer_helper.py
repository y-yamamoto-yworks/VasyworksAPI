"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.conf import settings
from lib.convert import *
from lib.functions import *


class SerializerHelper:
    """シリアライザ用のヘルパークラス"""
    @staticmethod
    def get_building_picture_fields():
        """建物画像用の項目"""
        return (
            'id',
            'building_oid',
            'picture_type',
            'thumbnail_file_url',
            'small_file_url',
            'medium_file_url',
            'large_file_url',
            'comment',
        )

    @staticmethod
    def get_room_picture_fields():
        """部屋画像用の項目"""
        return (
            'id',
            'building_oid',
            'room_oid',
            'picture_type',
            'thumbnail_file_url',
            'small_file_url',
            'medium_file_url',
            'large_file_url',
            'comment',
        )
