"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class StructureSerializer(serializers.ModelSerializer):
    """構造"""
    class Meta:
        model = Structure
        fields = ('id', 'name', 'short_name', )
