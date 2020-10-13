"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *


class MonthDaySerializer(serializers.ModelSerializer):
    """月間日付"""
    class Meta:
        model = MonthDay
        fields = ('id', 'name', 'from_day', 'to_day',)
