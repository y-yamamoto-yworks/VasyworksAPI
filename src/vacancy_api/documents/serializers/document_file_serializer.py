"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from lib.serializer_helper import SerializerHelper
from rent_db.models import *
from master.serializers import *


class DocumentFileSerializer(serializers.ModelSerializer):
    """書類ファイル"""
    class Meta:
        model = DocumentFile
        fields = (
            'id',
            'idb64',
            'file_title',
            'file_url',
            'comment',
        )
