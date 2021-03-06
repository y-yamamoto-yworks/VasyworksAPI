"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from .views import *

urlpatterns = [
    path('<str:key>', DocumentFileViewSet.as_view({'get': 'list'}), name='documents_index'),
]
