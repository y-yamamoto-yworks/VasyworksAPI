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
        fields = SerializerHelper.get_room_picture_fields()
