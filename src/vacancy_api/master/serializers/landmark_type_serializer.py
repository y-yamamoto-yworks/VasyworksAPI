"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class LandmarkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandmarkType
        fields = ('id', 'name',)
