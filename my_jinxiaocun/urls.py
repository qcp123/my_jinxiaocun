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
    re_path('order_manage/', order_manage),  # 批次管理
    re_path('goods_sell/', goods_sell),  # 商品销售
    re_path('sell_report/', sell_report),  # 销售报表
    re_path('vip_manage/', vip_manage),  # 会员管理
    re_path(r'login_action/', login_action),   #登录操作
    re_path(r'register_action/', register_action),   #注册
    re_path(r"save_goods/",save_goods),    #商品入库操作
    re_path(r"tiaoma_select/",tiaoma_select),    #商品销售根据条码查询商品
    re_path(r'change_goods_info/',change_goods_info),    #修改商品信息
    re_path(r'^del_goods/(?P<id>.*)/$',del_goods),    #删除商品
    re_path(r"^get_goods_info/$",get_goods_info),      #修改商品打开商品弹窗获取商品信息
    re_path(r"^select_customer_info/$",select_customer_info),      #查询会员信息
    re_path(r"^add_order/$",add_order),      #生成销售订单
    re_path(r"^goods_select/$",goods_select),      #根据筛选条件查询商品信息
    re_path(r"^add_customer/$",add_customer),      #添加会员
    re_path(r"^del_customer/$",del_customer),      #删除会员
    re_path(r"^select_vip/$",select_vip),      #查询会员信息
    re_path(r"^total_sell/$",total_sell),      #查询总收入
    re_path(r"^crash_income/$",crash_income),      #现金总收入
    re_path(r"^Alipay_income/$",Alipay_income),      #支付宝总收入
    re_path(r"^wechat_income/$",wechat_income),      #微信总收入
    re_path(r"^swipe_income/$",swipe_income),      #刷卡总收入
    re_path(r"^cangku_sell/$",cangku_sell),      #仓库销量
]
