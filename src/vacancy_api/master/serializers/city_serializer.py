"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from .pref_serializer import PrefSerializer


class CitySerializer(serializers.ModelSerializer):
    """市区町村"""
    pref = PrefSerializer(many=False)

    class Meta:
        model = City
        fields = ('id', 'idb64', 'name', 'lat', 'lng', 'pref',)
