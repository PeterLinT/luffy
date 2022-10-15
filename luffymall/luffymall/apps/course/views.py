from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Course, CourseCategory, CourseChapter

from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from .filter import CourseFilter
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView

from .serializers import CourseChapterSerializer, CourseModelSerializer, CourseRetrieveSerializer, \
    CourseCategoryModelSerializer


class CourseCategoryListAPIView(ListAPIView):
    queryset = CourseCategory.objects.filter(is_show=True, is_deleted=False).order_by("id")
    serializer_class = CourseCategoryModelSerializer


class CustomPageNumberPagination(PageNumberPagination):
    # page_query_param = "" # 地址上面代表页码的变量名，默认为page
    page_size = 5  # 每一页显示的数据量，没有设置页码，则不进行分页
    # 允许客户端通过指定的参数名来设置每一页数据量的大小，默认是size
    page_size_query_param = "size"
    max_page_size = 20  # 限制每一页最大展示的数据量


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.filter(is_deleted=False, is_show=True).order_by("orders")
    serializer_class = CourseModelSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = CourseFilter
    ordering_field = ('id', 'students', 'price')
    # ordering_fields = ('id', 'students', 'price')
    pagination_class = CustomPageNumberPagination


class CourseRetrieveAPIView(RetrieveAPIView):
    queryset = Course.objects.filter(is_deleted=False, is_show=True)
    serializer_class = CourseRetrieveSerializer


class CourseChapterListAPIView(ListAPIView):
    queryset = CourseChapter.objects.filter(is_deleted=False, is_show=True).order_by("chapter")
    serializer_class = CourseChapterSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['course', ]
