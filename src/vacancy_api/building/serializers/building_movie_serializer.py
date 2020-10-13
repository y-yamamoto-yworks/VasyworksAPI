"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import serializers
from rent_db.models import *
from master.serializers import *


class BuildingMovieSerializer(serializers.ModelSerializer):
    """建物動画"""
    movie_type = MovieTypeSerializer(many=False)

    class Meta:
        model = BuildingMovie
        fields = (
            'id',
            'idb64',
            'building_oid',
            'movie_type',
            'file_url',
            'comment',
        )
