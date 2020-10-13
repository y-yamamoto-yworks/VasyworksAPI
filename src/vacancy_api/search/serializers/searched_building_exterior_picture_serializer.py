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


class SearchedBuildingExteriorPictureSerializer(serializers.ModelSerializer):
    """検索建物の外観写真"""
    picture_type = PictureTypeSerializer(many=False)

    class Meta:
        model = SearchedBuildingExteriorPicture
        fields = SerializerHelper.get_building_picture_fields()
