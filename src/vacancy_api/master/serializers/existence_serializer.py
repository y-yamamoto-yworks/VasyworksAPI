"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class ExistenceSerializer(serializers.ModelSerializer):
    """有無"""
    class Meta:
        model = Existence
        fields = ('id', 'name', 'is_exists', 'is_none',)
