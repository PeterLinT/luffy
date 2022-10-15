# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path(r'banner/', views.BannerListAPIview.as_view()),
    path("nav/header/", views.NavHeaderListAPIView.as_view()),
    path("nav/footer/", views.NavFooterListAPIView.as_view()),
]
