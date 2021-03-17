"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *
from .building_picture_serializer import BuildingPictureSerializer


class BuildingFacilitySerializer(serializers.ModelSerializer):
    """建物周辺施設"""
    facility = FacilitySerializer(many=False)
    building_picture = BuildingPictureSerializer(many=False)

    class Meta:
        model = BuildingFacility
        fields = (
            'building_oid',
            'facility',
            'facility_name',
            'distance',
            'building_picture',
        )
