"""
System Name: Vasyworks
Project Name: vacancy_api
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from rest_framework import pagination
from rest_framework.response import Response


class ListApiPagination(pagination.LimitOffsetPagination):
    """リスト用ページネーション"""
    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'limit': self.limit,
            'offset': self.offset,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'list': data
        })


class MasterListApiPagination(pagination.PageNumberPagination):
    """Masterリスト用ページネーション"""
    page_size = 10000
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response({
            'count': len(data),
            'list': data
        })


class DataLinkListApiPagination(pagination.PageNumberPagination):
    """データ連携リスト用ページネーション"""
    page_size = 99999
    max_page_size = 99999

    def get_paginated_response(self, data):
        return Response({
            'count': len(data),
            'list': data
        })
