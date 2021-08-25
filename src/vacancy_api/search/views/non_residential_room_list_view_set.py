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
from search.serializers import SearchedRoomSerializer


class NonResidentialRoomListViewSet(viewsets.ReadOnlyModelViewSet):
    """非居住用部屋リスト"""
    conditions = None

    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        self.conditions = SearchConditions()
        self.conditions.set_conditions(self.request.query_params)

        self.queryset = SearchedRoom.get_rooms(
            conditions=self.conditions,
            is_residential=False,
        )
        self.serializer_class = SearchedRoomSerializer

        return super().list(request, args, kwargs)
