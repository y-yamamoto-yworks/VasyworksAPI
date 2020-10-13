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
from building.serializers import BuildingSerializer


class BuildingViewSet(viewsets.ReadOnlyModelViewSet):
    """建物"""
    is_no_limit = False         # 自社物件以外も含む場合はTrue
    is_only_residential = False      # 居住用のみ対象の場合はTrue
    is_only_non_residential = False  # 非居住用のみ対象の場合はTrue

    def retrieve(self, request, *args, **kwargs):
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

        oid = kwargs['oid']

        conditions = Q(oid=oid, is_hidden_web=False, is_deleted=False)
        if not self.is_no_limit:
            conditions.add(Q(
                Q(management_type__is_own=True)     # 自社物件
                | Q(management_type__is_entrusted=True)     # 専任物件
                | Q(management_type__is_condo_management=True)      # 分譲マンション
            ), Q.AND)

        self.queryset = Building.objects.filter(conditions)
        self.serializer_class = BuildingSerializer
        self.lookup_field = 'oid'

        return super().retrieve(request, args, kwargs)

    def get_object(self):
        """建物インスタンスを取得"""
        instance = super().get_object()

        instance.is_no_limit = self.is_no_limit
        instance.is_only_residential = self.is_only_residential
        instance.is_only_non_residential = self.is_only_non_residential

        return instance
