from django.db import models

# Create your models here.

from django.db import models


class goods(models.Model):    #商品表
    goods_id=models.CharField(max_length=5,null=True)
    batchname=models.CharField(max_length=5,null=True)      #批次名称
    goodsserial=models.CharField(max_length=20,null=True)   #商品编号
    barcode=models.CharField(max_length=20,null=True)      #商品条码
    goodsname=models.CharField(max_length=20,null=True)    #商品名称
    goodstype=models.CharField(max_length=20,null=True)    #商品类型
    inputsize=models.CharField(max_length=20,null=True)    #商品尺码
    quantity=models.CharField(max_length=20,null=True)     #商品数量
    totalprice=models.CharField(max_length=20,null=True)   #商品售价
    cangku=models.CharField(max_length=20,null=True)       #仓库
    costunitprice=models.CharField(max_length=20,null=True)
    costtotalprice=models.CharField(max_length=20,null=True)
    username=models.CharField(max_length=10,null=True)
    beizhu=models.CharField(max_length=500)

    def __str__(self):
        return self.goodsname

#客户表
class customer(models.Model):
    customer_name=models.CharField(max_length=20,null=True)   #客户姓名
    customer_phone=models.CharField(max_length=20,null=True)       #手机号
    customer_sex=models.CharField(max_length=20,null=True)    #性别
    customer_jifen=models.CharField(max_length=20,null=True)   #积分
    customer_total_buy=models.CharField(max_length=20,null=True)   #消费总额

    def __str__(self):
        return self.customer_name

# 订单表
class order(models.Model):
    order_id=models.CharField(max_length=20,null=True)       #订单ID
    customer_phone=models.CharField(max_length=20,null=True)   #用户手机号
    goods_chima=models.CharField(max_length=20,null=True)       #商品尺码
    goods_huohao=models.CharField(max_length=20,null=True)         #商品货号
    goods_name=models.CharField(max_length=20,null=True)            #商品名称
    sell_price=models.CharField(max_length=20,null=True)            #出售价格
    goods_type=models.CharField(max_length=20,null=True)        #商品类型
    goods_pici=models.CharField(max_length=20,null=True)        #商品批次
    goods_tiaoma=models.CharField(max_length=20,null=True)      #商品条码
    goods_cangku=models.CharField(max_length=20,null=True)      #所属仓库
    goods_shuliang=models.CharField(max_length=20,null=True)    #出售数量
    pay_type=models.CharField(max_length=20,null=True)          #支付方式
    create_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.goods_name+'       '+self.order_id


