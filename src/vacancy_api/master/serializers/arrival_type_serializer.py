"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class ArrivalTypeSerializer(serializers.ModelSerializer):
    """到着種別"""
    class Meta:
        model = ArrivalType
        fields = ('id', 'name',)
