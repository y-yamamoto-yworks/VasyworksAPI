"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import urllib.parse
import django_filters
from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets, filters
from django.db.models import Q
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text, escape_uri_path
from lib.convert import *
from lib.api_helper import ApiHelper
from rent_db.models import *
from company.serializers import CompanySerializer


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """会社"""
    def retrieve(self, request, *args, **kwargs):
        key = kwargs.get('key')
        if not ApiHelper.check_key(key):
            raise Exception

        conditions = Q(pk=settings.COMPANY_ID)
        self.queryset = Company.objects.filter(conditions)
        self.serializer_class = CompanySerializer

        return super().retrieve(request, args, kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        instance = queryset.first()
        return instance
