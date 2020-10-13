"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class VacancyStatusSerializer(serializers.ModelSerializer):
    """空室状況"""
    class Meta:
        model = VacancyStatus
        fields = ('id', 'name',)
