"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class FacilitySerializer(serializers.ModelSerializer):
    """周辺施設"""
    class Meta:
        model = Facility
        fields = ('id', 'name',)
