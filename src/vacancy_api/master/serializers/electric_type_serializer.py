"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class ElectricTypeSerializer(serializers.ModelSerializer):
    """電気種別"""
    class Meta:
        model = ElectricType
        fields = ('id', 'name',)
