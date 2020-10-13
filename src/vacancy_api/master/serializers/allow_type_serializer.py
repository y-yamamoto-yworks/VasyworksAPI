"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class AllowTypeSerializer(serializers.ModelSerializer):
    """許可種別"""
    class Meta:
        model = AllowType
        fields = ('id', 'name',)
