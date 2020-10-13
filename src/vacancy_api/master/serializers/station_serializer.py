"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from .railway_serializer import RailwaySerializer


class StationSerializer(serializers.ModelSerializer):
    """駅"""
    railway = RailwaySerializer(many=False)

    class Meta:
        model = Station
        fields = ('id', 'idb64', 'name', 'railway',)
