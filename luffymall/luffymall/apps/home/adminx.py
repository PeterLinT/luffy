# -*- coding:utf-8 -*-
import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "路飞学城"  # 设置站点标题
    site_footer = "路飞学城有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)

# 轮播图
from .models import Banner
class BannerInfoModelAdmin(object):
    list_display=["title","orders","is_show"]
xadmin.site.register(Banner, BannerInfoModelAdmin)

from .models import Nav
class NavModelAdmin(object):
    list_display=["title","link","is_show","is_site","position"]
xadmin.site.register(Nav, NavModelAdmin)