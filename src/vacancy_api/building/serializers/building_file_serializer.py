"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *


class BuildingFileSerializer(serializers.ModelSerializer):
    """建物ファイル"""

    class Meta:
        model = BuildingFile
        fields = (
            'id',
            'idb64',
            'building_oid',
            'file_title',
            'file_url',
            'comment',
        )
