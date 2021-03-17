"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *


class BuildingPanoramaSerializer(serializers.ModelSerializer):
    """建物パノラマ"""
    panorama_type = PanoramaTypeSerializer(many=False)

    class Meta:
        model = BuildingPanorama
        fields = (
            'building_oid',
            'panorama_type',
            'file_url',
            'comment',
        )
