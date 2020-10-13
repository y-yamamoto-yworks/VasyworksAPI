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
from rent_db.models import *
from common.pagination import *
from master.serializers import AreaSerializer


class AreaViewSet(viewsets.ReadOnlyModelViewSet):
    """エリア"""
    pagination_class = MasterListApiPagination

    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        city_id = kwargs.get('city_id')

        self.queryset = Area.objects.filter(
            Q(is_stopped=False, city_area_cities__id=city_id) | Q(pk=0)
        ).order_by('pref__priority', 'kana')
        self.serializer_class = AreaSerializer

        return super().list(request, args, kwargs)
