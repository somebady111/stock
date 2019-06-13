from django.db import models
from userinfo.models import *
from stocks.models import *
# Create your models here.

class SelfStock(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    stock = models.ForeignKey(Stock,verbose_name='股票')

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = verbose_name_plural = '自选股票表'


class DealStock(models.Model):
    dealtime = models.DateTimeField(verbose_name='交易时间',auto_now_add=True)
    stock = models.CharField(verbose_name='股票',max_length=50,null=True)
    amount = models.IntegerField(verbose_name='数量',null=True)
    price = models.DecimalField(verbose_name='价格',max_digits=8,decimal_places=2,default=0,null=True)
    suser = models.ForeignKey(UserInfo,verbose_name='卖家',related_name='sname')
    buser = models.ForeignKey(UserInfo,verbose_name='买家',related_name='bname')

    def __str__(self):
        return self.stock
    class Meta:
        verbose_name = verbose_name_plural = '记录表'


class BOSStock(models.Model):
    ROLE = (
        (0,'买'),
        (1,'卖'),
    )
    role = models.IntegerField(verbose_name='买卖角色',choices=ROLE,default=0)
    stock = models.ForeignKey(Stock,verbose_name='股票',null=True)
    amount = models.IntegerField(verbose_name='数量',null=True)
    price = models.DecimalField(verbose_name='价格',max_digits=8,decimal_places=2,default=0)
    user = models.ForeignKey(UserInfo,verbose_name='用户',null=True)
    datetime = models.DateTimeField(verbose_name='时间',auto_now_add=True)

    def __str__(self):
        return self.role
    class Meta:
        verbose_name = verbose_name_plural = '挂单表'