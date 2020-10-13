"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from .pref_serializer import PrefSerializer


class ElementarySchoolSerializer(serializers.ModelSerializer):
    """小学校区"""
    pref = PrefSerializer(many=False)

    class Meta:
        model = ElementarySchool
        fields = ('id', 'name', 'lat', 'lng', 'pref',)
