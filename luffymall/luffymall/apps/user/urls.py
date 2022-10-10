# -*- coding:utf-8 -*-
from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path(r'login/', obtain_jwt_token),
    path(r"register/", views.RegisterView.as_view()),
]
