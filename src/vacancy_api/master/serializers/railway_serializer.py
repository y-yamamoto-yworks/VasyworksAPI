"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class RailwaySerializer(serializers.ModelSerializer):
    """鉄道沿線"""
    class Meta:
        model = Railway
        fields = ('id', 'idb64', 'name', 'short_name', )
