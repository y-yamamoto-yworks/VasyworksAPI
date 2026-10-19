"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 - 2026 Yasuhiro Yamamoto
"""
from django.urls import include, path
from .views import *

urlpatterns = [
    path('departments/', DepartmentViewSet.as_view({'get': 'list'}), name='company_departments'),
    path('staffs/', StaffViewSet.as_view({'get': 'list'}), name='company_staffs'),
    path('staffs/<int:department_id>', StaffViewSet.as_view({'get': 'list'}), name='company_staffs'),
    path('', CompanyViewSet.as_view({'get': 'retrieve'}), name='company_detail'),
]
