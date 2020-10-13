"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class BuildingTypeSerializer(serializers.ModelSerializer):
    """建物種別"""
    class Meta:
        model = BuildingType
        fields = ('id', 'name', 'is_residential', 'is_building',)
