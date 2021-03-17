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
from data_link.serializers import RoomSerializer


class VacancyRoomViewSet(viewsets.ReadOnlyModelViewSet):
    """空室"""
    pagination_class = DataLinkListApiPagination
    is_no_limit = False         # 自社物件以外も含む場合はTrue
    is_only_residential = False      # 居住用のみ対象の場合はTrue
    is_only_non_residential = False  # 非居住用のみ対象の場合はTrue

    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        param = request.GET.get('no_lmt', None)
        if param:
            if param == '1' or param.lower() == 'true':
                self.is_no_limit = True

        param = request.GET.get('only_res', None)
        if param:
            if param == '1' or param.lower() == 'true':
                self.is_only_residential = True

        param = request.GET.get('only_no_res', None)
        if param:
            if param == '1' or param.lower() == 'true':
                self.is_only_non_residential = True

        conditions = Room.get_vacancy_room_condition(
                self.is_no_limit,
                self.is_only_residential,
                self.is_only_non_residential
            )

        # 追加条件があればここで追加する。

        self.queryset = Room.objects.filter(conditions).order_by('building__id', 'room_no')
        self.serializer_class = RoomSerializer

        return super().list(request, args, kwargs)
