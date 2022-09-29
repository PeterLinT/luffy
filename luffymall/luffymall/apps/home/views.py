from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerModelSerializers
from luffymall.settings import constants


class BannerListAPIview(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by('-orders', '-id')[
               :constants.BANNER_LENGTH]
    serializer_class = BannerModelSerializers


from .models import Nav
from .serializers import NavModelSerializer


class NavHeaderListAPIView(ListAPIView):
    """导航菜单视图"""
    queryset = Nav.objects.filter(is_show=True, is_deleted=False, position=1).order_by("orders", "-id")[
               :constants.HEADER_NAV_LENGTH]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(ListAPIView):
    """导航菜单视图"""
    queryset = Nav.objects.filter(is_show=True, is_deleted=False, position=2).order_by("orders", "id")[
               :constants.FOOTER_NAV_LENGTH]
    serializer_class = NavModelSerializer
