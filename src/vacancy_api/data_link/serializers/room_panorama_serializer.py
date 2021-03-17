"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *


class RoomPanoramaSerializer(serializers.ModelSerializer):
    """部屋パノラマ"""
    panorama_type = PanoramaTypeSerializer(many=False)

    class Meta:
        model = RoomPanorama
        fields = (
            'building_oid',
            'room_oid',
            'panorama_type',
            'file_url',
            'comment',
        )
