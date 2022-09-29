# -*- coding:utf-8 -*-
from django.urls import path
from .views import BannerListAPIview
urlpatterns = [
    path(r'banner/', BannerListAPIview.as_view())
]