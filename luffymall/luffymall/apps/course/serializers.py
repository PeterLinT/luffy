# -*- coding:utf-8 -*-
# 开发中一个序列化器 A 中需要同时序列化其他模型 B 的数据返回给客户端,那么直接通过外键默认只会返回主键ID
# 所以我们可以通过再创建一个模型B的序列化器,对模型B的数据进行序列化
# 在序列化器A中直接把模型B的序列化器调用作为字段值来声明即可.

from rest_framework import serializers
from .models import CourseCategory, Course, Teacher, CourseChapter, CourseLesson


class CourseCategoryModelSerializer(serializers.ModelSerializer):
    """课程分类的序列化器"""

    class Meta:
        model = CourseCategory
        fields = ("id", "name")


class CourseTeacherModelSerializer(serializers.ModelSerializer):
    """课程所属老师的序列化器"""

    class Meta:
        model = Teacher
        fields = ("name", "title", "signature", 'image', 'brief',)


class CourseModelSerializer(serializers.ModelSerializer):
    """课程信息的序列化器"""
    teacher = CourseTeacherModelSerializer()  # 老师 1 : 多课程

    # teacher = CourseTeacherModelSerializer(many=True) # 多对1
    class Meta:
        model = Course
        fields = ("id", "name", "course_img", "students", "lessons", "pub_lessons", "price", "teacher", 'lessons_list',
                  'course_category','real_price')


class CourseRetrieveSerializer(serializers.ModelSerializer):
    teacher = CourseTeacherModelSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img", "students", "lessons", "pub_lessons", "price", "teacher", "brief",
                  "level_name", 'brief_html', 'course_video', ]


class CourseLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLesson
        fields = ["id", "name", "duration", "free_trail"]


class CourseChapterSerializer(serializers.ModelSerializer):
    coursesections = CourseLessonSerializer(many=True)

    class Meta:
        model = CourseChapter
        fields = ["chapter", "name", "summary", "coursesections"]
