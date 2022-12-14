# -*- coding:utf-8 -*-
import xadmin

from .models import CourseCategory


class CourseCategoryModelAdmin(object):
    """课程分类模型管理类"""
    pass


xadmin.site.register(CourseCategory, CourseCategoryModelAdmin)

from .models import Course


class CourseModelAdmin(object):
    """课程模型管理类"""
    pass


xadmin.site.register(Course, CourseModelAdmin)

from .models import Teacher


class TeacherModelAdmin(object):
    """老师模型管理类"""
    pass


xadmin.site.register(Teacher, TeacherModelAdmin)

from .models import CourseChapter


class CourseChapterModelAdmin(object):
    """课程章节模型管理类"""
    pass


xadmin.site.register(CourseChapter, CourseChapterModelAdmin)

from .models import CourseLesson


class CourseLessonModelAdmin(object):
    """课程课时模型管理类"""
    pass


xadmin.site.register(CourseLesson, CourseLessonModelAdmin)
from .models import CourseExpire


class CourseExpireModelAdmin(object):
    """商品有效期模型"""
    pass


xadmin.site.register(CourseExpire, CourseExpireModelAdmin)
from .models import CourseDiscountType


class CourseDiscountTypeModelAdmin(object):
    """价格优惠类型"""
    pass


xadmin.site.register(CourseDiscountType, CourseDiscountTypeModelAdmin)

from .models import CourseDiscount


class CourseDiscountModelAdmin(object):
    """价格优惠公式"""
    pass


xadmin.site.register(CourseDiscount, CourseDiscountModelAdmin)

from .models import CoursePriceDiscount


class CoursePriceDiscountModelAdmin(object):
    """价格优惠公式"""
    pass


xadmin.site.register(CoursePriceDiscount, CoursePriceDiscountModelAdmin)

from .models import Activity


class ActivityModelAdmin(object):
    """商品活动模型"""
    pass


xadmin.site.register(Activity, ActivityModelAdmin)
