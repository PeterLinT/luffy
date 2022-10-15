# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Banner
from .models import Nav
class BannerModelSerializers(serializers.ModelSerializer):
    '''轮播广告的序列化器'''
    # 模型序列化器字段声明
    class Meta:
        model = Banner
        fields = ['image_url','link']
class NavModelSerializer(serializers.ModelSerializer):
    """导航菜单序列化器"""
    class Meta:
        model = Nav
        fields = ["title","link","is_site"]