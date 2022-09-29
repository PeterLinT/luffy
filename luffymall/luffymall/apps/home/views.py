from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializer import BannerModelSerializers
from luffymall.settings import constants


class BannerListAPIview(ListAPIView):
    queryset = Banner.objects.filter(is_show=True,is_deleted=False).order_by('-orders','-id')[:constants.BANNER_LENGTH]
    serializer_class = BannerModelSerializers


