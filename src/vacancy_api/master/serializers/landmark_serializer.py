"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from .landmark_type_serializer import LandmarkTypeSerializer


class LandmarkSerializer(serializers.ModelSerializer):
    landmark_type = LandmarkTypeSerializer(many=False)

    class Meta:
        model = Landmark
        fields = (
            'id',
            'name',
            'kana',
            'short_name',
            'lat',
            'lng',
            'landmark_type',
        )
