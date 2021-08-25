"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import urllib.parse
import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text, escape_uri_path
from lib.convert import *
from lib.api_helper import ApiHelper
from common.pagination import *
from search.models import *
from search.serializers import SearchedBuildingSerializer


class BuildingListViewSet(viewsets.ReadOnlyModelViewSet):
    """居住用建物リスト"""
    conditions = None

    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        self.conditions = SearchConditions()
        self.conditions.set_conditions(self.request.query_params)

        self.queryset = SearchedBuilding.get_buildings(
            conditions=self.conditions,
            is_residential=True,
        )
        self.serializer_class = SearchedBuildingSerializer

        return super().list(request, args, kwargs)

    def paginate_queryset(self, queryset):
        """建物インスタンスに設定"""
        items = super().paginate_queryset(queryset)
        for item in items:
            item.conditions = self.conditions
            item.is_residential = True
        return items

