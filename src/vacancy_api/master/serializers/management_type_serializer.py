"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class ManagementTypeSerializer(serializers.ModelSerializer):
    """管理種別"""
    class Meta:
        model = ManagementType
        fields = ('id', 'name', 'is_own', 'is_entrusted', 'is_condo_management',)
