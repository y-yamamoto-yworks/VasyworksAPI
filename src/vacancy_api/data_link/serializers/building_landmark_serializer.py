"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *


class BuildingLandmarkSerializer(serializers.ModelSerializer):
    """建物ランドマーク"""
    landmark = LandmarkSerializer(many=False)

    class Meta:
        model = BuildingLandmark
        fields = (
            'building_oid',
            'landmark',
            'distance',
        )
