"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class DirectionSerializer(serializers.ModelSerializer):
    """方向"""
    class Meta:
        model = Direction
        fields = ('id', 'name',)
