from my_app.models import *
import json
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
import random
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Count,Avg,Max,Min,Sum
from django.db import models
from django.db.models import Q


def welcome(request):   #公共页面
    return render(request,'welcome.html')

def child(request,eid,oid):   #页面分发器
    res=child_json(eid)
    return render(request,eid,res)

def child_json(eid):
    res={}
    if eid=='select_goods.html':    #商品查询页面
        date=goods.objects.all()
        res={'goods':date}
        return res
    if eid=="goods_sell.html":     #商品销售页面
        date = goods.objects.all()
        res = {'goods': date}
    if eid=='vip_manage.html':     #会员管理页面
        data=customer.objects.all()
        res={"customer_info":data}
        return res
    if eid=='order_manage.html':     #订单管理页面
        data=order.objects.all()
        res={"order_info":data}
        return res




def login(request):   #登录
    return render(request,'login.html')


def home(request):   #首页
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})


def goods_save(request):   #商品入库
    return render(request,'welcome.html',{"whichHTML":"goods_save.html","oid":""})

def select_goods(request):   #库存查询
    return render(request,'welcome.html',{"whichHTML":"select_goods.html","oid":""})


def order_manage(request):   #订单管理
    page=request.GET.get("page")
    return render(request,'welcome.html',{"whichHTML":"order_manage.html","oid":""})


def goods_sell(request):   #商品销售
    return render(request,'welcome.html',{"whichHTML":"goods_sell.html","oid":""})


def sell_report(request):   #销售报表
    return render(request,'welcome.html',{"whichHTML":"sell_report.html","oid":""})


def vip_manage(request):   #会员管理
    return render(request,'welcome.html',{"whichHTML":"vip_manage.html","oid":""})



def login_action(request):    #登录
    username=request.GET['username']
    password=request.GET['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        return HttpResponse('success')
    else:
        return HttpResponse('用户名或密码错误！')

#注册
def register_action(request):
    username = request.GET['username']
    password = request.GET['password']
    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return HttpResponse('注册成功')
    except:
        return HttpResponse('用户名已存在~')

#商品入库操作
def save_goods(request):
    pici=request.GET['pici']
    huohao=request.GET['huohao']
    goods_name=request.GET['goods_name']
    price=request.GET['price']
    tiaoma=request.GET['tiaoma']
    chima=request.GET['chima']
    shuliang=request.GET['shuliang']
    pinlei=request.GET['pinlei']
    cangku=request.GET['cangku']
    beizhu=request.GET['beizhu']
    if pici and huohao and goods_name and price and tiaoma and chima and shuliang and pinlei and cangku != '':
        goods.objects.create(batchname=pici,goodsserial=huohao,goodsname=goods_name,
                         totalprice=price,barcode=tiaoma,inputsize=chima,quantity=shuliang,
                         goodstype=pinlei,cangku=cangku,beizhu=beizhu)
        return HttpResponse("success")
    elif pici =='':
        return HttpResponse("录入失败，商品批次不能为空~")
    elif huohao =='':
        return HttpResponse("录入失败，商品货号不能为空~")
    elif goods_name =='':
        return HttpResponse("录入失败，商品名称不能为空~")
    elif price =='':
        return HttpResponse("录入失败，商品价格不能为空~")
    elif tiaoma =='':
        return HttpResponse("录入失败，商品条码不能为空~")
    elif chima =='':
        return HttpResponse("录入失败，商品尺码不能为空~")
    elif shuliang =='':
        return HttpResponse("录入失败，商品数量不能为空~")
    elif pinlei =='':
        return HttpResponse("录入失败，商品类型不能为空~")
    elif cangku =='':
        return HttpResponse("录入失败，仓库不能为空~")


    return HttpResponse('')


#商品销售根据商品条码查询商品
def tiaoma_select(request):
    tiaoma=request.GET["tiaoma_select"]
    if tiaoma is not None:
        try:
            goods_info = goods.objects.filter(barcode=tiaoma).values()[0]
            return HttpResponse(json.dumps(goods_info),content_type="application/json")
        except:
            return HttpResponse('商品不存在，请确认商品条码是否正确')
    elif tiaoma=='':
        return HttpResponseRedirect('请输入条码！')


#删除商品
def del_goods(request,id):
    goods_id=goods.objects.filter(id=id)[0].id
    goods.objects.filter(id=goods_id).delete()
    return HttpResponseRedirect("/select_goods/")


#修改商品信息时打开弹窗获取商品信息
def get_goods_info(request):
    goods_id=request.GET['goods_id']
    goods_info=goods.objects.filter(id=goods_id).values()[0]
    # json.dumps(your_data, default=str)
    return HttpResponse(json.dumps(goods_info),content_type="application/json")

#修改商品信息
def change_goods_info(request):
    id=request.GET["id"]
    pici = request.GET['pici']
    huohao = request.GET['huohao']
    goods_name = request.GET['goods_name']
    price = request.GET['price']
    tiaoma = request.GET['tiaoma']
    chima = request.GET['chima']
    shuliang = request.GET['shuliang']
    pinlei = request.GET['pinlei']
    cangku = request.GET['cangku']
    beizhu = request.GET['beizhu']
    if pici and huohao and goods_name and price and tiaoma and chima and shuliang and pinlei and cangku is not None:
        goods.objects.filter(id=id).update(batchname=pici, goodsserial=huohao, goodsname=goods_name,
                             totalprice=price, barcode=tiaoma, inputsize=chima, quantity=shuliang,
                             goodstype=pinlei, cangku=cangku, beizhu=beizhu)
        return HttpResponse("success")
    elif pici =='':
        return HttpResponse("修改商品失败，批次不能为空~")
    elif huohao =='':
        return HttpResponse("修改商品失败，货号不能为空~")
    elif goods_name =='':
        return HttpResponse("修改商品失败，商品名称不能为空~")
    elif price =='':
        return HttpResponse("修改商品失败，价格不能为空~")
    elif tiaoma =='':
        return HttpResponse("修改商品失败，条码不能为空~")
    elif chima =='':
        return HttpResponse("修改商品失败，尺码不能为空~")
    elif shuliang =='':
        return HttpResponse("修改商品失败，数量不能为空~")
    elif pinlei =='':
        return HttpResponse("修改商品失败，品类不能为空~")
    elif cangku =='':
        return HttpResponse("修改商品失败，仓库不能为空~")


#查询会员信息
def select_customer_info(request):
    customer_phone=request.GET['customer_phone']
    if customer_phone !='':
        try:
            customer_info=customer.objects.filter(customer_phone=customer_phone).values()[0]
            return HttpResponse(json.dumps(customer_info), content_type="application/json")
        except:
            return HttpResponse('会员不存在，请确认手机号是否正确')
    elif customer_phone=='':
        return HttpResponse("请输入会员手机号~")

#新增订单
def add_order(request):
    goods_name=request.GET['goods_name']
    tiaoma=request.GET['tiaoma']
    huohao=request.GET['huohao']
    chima=request.GET['chima']
    price=request.GET['price']
    shuliang=request.GET['shuliang']
    cangku=request.GET['cangku']
    sell_price=request.GET['sell_price']
    pay_type=request.GET['pay_type']
    phone_number=request.GET['phone_number']
    coustomer_name=request.GET['coustomer_name']
    total_jifen=request.GET['total_jifen']
    if goods_name and tiaoma and huohao and chima and price and shuliang and cangku and sell_price and pay_type and phone_number and coustomer_name and total_jifen is not None:
        del_shulaing = goods.objects.filter(barcode=tiaoma).values()[0]
        shuliang_del = del_shulaing["quantity"]
        goods.objects.filter(barcode=tiaoma).update(quantity=str(int(shuliang_del) - int(shuliang)))
        customer.objects.filter(customer_phone=phone_number).update(customer_jifen=total_jifen)
        customer_pay_money=customer.objects.filter(customer_phone=phone_number).values()[0]
        customer_pay_money1=customer_pay_money["customer_total_buy"]
        customer.objects.filter(customer_phone=phone_number).update(customer_total_buy=str(int(customer_pay_money1)+int(sell_price)))
        order.objects.create(
            order_id=random.randint(11111111,99999999),
            customer_phone=phone_number,
            goods_chima=chima,
            goods_huohao=huohao,
            goods_name=goods_name,
            sell_price=sell_price,
            goods_tiaoma=tiaoma,
            goods_cangku=cangku,
            goods_shuliang=shuliang,
            pay_type=pay_type,
        )
        return HttpResponse('订单已生成~')
    elif shuliang=='':
        return HttpResponse('订单生成失败，商品数量不可为空')
    elif phone_number=='':
        return HttpResponse('订单生成失败，请确认购买用户信息')
    elif coustomer_name=='' or total_jifen=='':
        return HttpResponse('订单生成失败，请确认用户信息')
    elif tiaoma=='' or goods_name=='' or huohao=='' or chima=='' or price=='' or cangku=='' or sell_price=='':
        return HttpResponse('订单生成失败，请确认商品信息')




#根据筛选条件查询商品信息
def goods_select(request):
    goods_name=request.GET['goods_name']
    goods_huohao=request.GET['goods_huohao']
    goods_tiaoma=request.GET['goods_tiaoma']
    goods_type=request.GET['goods_type']
    cagnku=request.GET['cagnku']

    if goods_name and goods_huohao and goods_tiaoma and goods_type and cagnku =='':
        goods_info=goods.objects.all()
        return HttpResponse(json.dumps(goods_info),content_type='application/json')
    else:
        goods_info=goods.objects.filter(
            goodsname=goods_name,
            goodsserial=goods_huohao,
            barcode=goods_tiaoma,
            goodstype=goods_type,
            cangku=cagnku,
        ).values()[0]
        return HttpResponse(json.dumps(goods_info), content_type='application/json')

#新增会员
def add_customer(request):
    customer_name=request.GET["customer_name"]
    customer_phone=request.GET["customer_phone"]
    customer_sex=request.GET["customer_sex"]

    if customer_name and customer_phone and customer_sex is not None:
        customer.objects.create(
            customer_name=customer_name,
            customer_phone=customer_phone,
            customer_sex=customer_sex)
        return HttpResponse("success")
    elif customer_name=="":
        return HttpResponse('请输入会员手机号~')
    elif customer_phone == "":
        return HttpResponse("请输入会员姓名~")


#删除顾客
def del_customer(request):
    id=request.GET["id"]
    customer_id=customer.objects.filter(id=id).values()[0]
    customer_id1=customer_id["id"]
    customer.objects.filter(id=customer_id1).delete()
    return HttpResponse("success")


# 查询顾客信息
def select_vip(request):
    customer_phone=request.GET["customer_phone"]
    if customer_phone == '':
        return HttpResponse("查询全部数据")
    elif customer_phone != '':
        try:
            vip_info=customer.objects.filter(customer_phone=customer_phone).values()[0]
            return HttpResponse(json.dumps(vip_info),content_type="application/json")
        except:
            return HttpResponse('未查询到数据')


# 销售总额
def total_sell(request):
    total_sell=order.objects.all().aggregate(Sum("sell_price"))
    return HttpResponse(json.dumps(total_sell),content_type="application/json")

