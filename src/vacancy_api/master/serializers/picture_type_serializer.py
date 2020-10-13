"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class PictureTypeSerializer(serializers.ModelSerializer):
    """画像種別"""
    class Meta:
        model = PictureType
        fields = ('id', 'name', 'is_building_exterior', 'is_layout',)
