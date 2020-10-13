"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from lib.serializer_helper import SerializerHelper
from master.serializers import *
from company.serializers import *
from search.models import *


class SearchedRoomInteriorPictureSerializer(serializers.ModelSerializer):
    """検索部屋の室内写真"""
    picture_type = PictureTypeSerializer(many=False)

    class Meta:
        model = SearchedRoomInteriorPicture
        fields = SerializerHelper.get_room_picture_fields()
