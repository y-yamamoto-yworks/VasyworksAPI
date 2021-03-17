"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from lib.serializer_helper import SerializerHelper
from rent_db.models import *
from master.serializers import *


class RoomPictureSerializer(serializers.ModelSerializer):
    """部屋画像"""
    picture_type = PictureTypeSerializer(many=False)

    class Meta:
        model = RoomPicture
        fields = (
            'building_oid',
            'room_oid',
            'picture_type',
            'thumbnail_file_url',
            'small_file_url',
            'medium_file_url',
            'large_file_url',
            'comment',
        )