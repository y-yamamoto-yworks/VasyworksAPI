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
from company.serializers import StaffSerializer


class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    """スタッフ"""
    pagination_class = MasterListApiPagination

    def list(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        department_id = kwargs.get('department_id')

        conditions = Q(
            is_stopped=False,
            is_deleted=False,
            is_publish_vacancy=True,
            department__is_stopped=False,
            department__is_deleted=False,
            department__is_publish_vacancy=True,
        )
        if department_id:
            conditions.add(Q(department_id=department_id), Q.AND)

        self.queryset = Staff.objects.filter(conditions).order_by('department__priority', 'priority', 'id')
        self.serializer_class = StaffSerializer

        return super().list(request, args, kwargs)
