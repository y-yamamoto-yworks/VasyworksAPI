"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
import urllib.parse
import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str, escape_uri_path
from lib.convert import *
from lib.api_helper import ApiHelper
from rent_db.models import *
from common.pagination import *
from master.serializers import WasherTypeSerializer


class WasherTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """洗濯機設置種別"""
    pagination_class = MasterListApiPagination

    def list(self, request, *args, **kwargs):
        if not ApiHelper.check_key(request):
            raise PermissionDenied("Permission denied")

        self.queryset = WasherType.objects.filter(is_stopped=False).order_by('priority')
        self.serializer_class = WasherTypeSerializer

        return super().list(request, args, kwargs)
