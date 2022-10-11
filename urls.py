"""my_jinxiaocun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from my_app.views import *

urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path('welcome/', welcome),  # 首页也
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", child),  # 分发器
    re_path('home/', home),
    re_path('login/', login),  # 登录
    re_path('goods_save/', goods_save),  # 商品入库
    re_path('select_goods/', select_goods),  # 库存查询
    re_path('batch_manage/', batch_manage),  # 批次管理
    re_path('goods_sell/', goods_sell),  # 商品销售
    re_path('sell_report/', sell_report),  # 销售报表
    re_path('vip_manage/', vip_manage),  # 会员管理
    re_path(r'login_action/', login_action),   #登录操作
    re_path(r'register_action/', register_action),   #注册
]
