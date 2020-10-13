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


class SearchedGaragePictureSerializer(serializers.ModelSerializer):
    """検索建物の外観写真"""
    class Meta:
        model = SearchedGaragePicture
        fields = (
            'id',
            'building_oid',
            'thumbnail_file_url',
            'small_file_url',
            'medium_file_url',
            'large_file_url',
            'comment',
        )
