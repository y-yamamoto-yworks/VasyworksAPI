"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class GarageStatusSerializer(serializers.ModelSerializer):
    """駐車場空き状況"""
    class Meta:
        model = GarageStatus
        fields = ('id', 'name',)
