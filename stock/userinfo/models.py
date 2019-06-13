from django.db import models
from django.contrib.auth.models import AbstractUser
from stocks.models import *
# Create your models here.

class UserInfo(AbstractUser):
    uemail = models.EmailField(verbose_name='邮箱',null=True)
    uphone = models.CharField(verbose_name='电话',max_length=11,null=True)
    isActive = models.BooleanField(verbose_name='是否激活',default=False)

    def __str__(self):
        return self.uemail
    class Meta:
        verbose_name = verbose_name_plural = '用户表'
        ordering = ['-id']


class Fund(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    money = models.DecimalField(verbose_name='资金',max_digits=8,decimal_places=2,default=0)
    frozen_money = models.DecimalField(verbose_name='冻结资金',max_digits=8,decimal_places=2,default=0)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = verbose_name_plural = '钱包表'

class Hold(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    stock = models.ForeignKey(Stock,verbose_name='股票')
    amount = models.IntegerField(blank=True,verbose_name='持仓数',null=True)
    frozen_amount = models.IntegerField(blank=True,verbose_name='冻结数量',null=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = verbose_name_plural = '持仓表'

class Bank(models.Model):
    BANK = (
        (0,'建设银行'),
        (1,'中国银行'),
        (2,'华夏银行'),
        (3,'花旗银行'),
        (4,'齐鲁银行'),
        (5,'青岛银行'),
        (6,'工商银行'),
        (7,'农业银行'),
    )
    user = models.ForeignKey(UserInfo,verbose_name='用户')
    truename = models.CharField(verbose_name='真实姓名',max_length=10,null=True)
    bank  = models.IntegerField(verbose_name='银行',choices=BANK,default=0,null=True)
    bankNo = models.CharField(verbose_name='银行卡号',max_length=24,null=True)
    tradepwd = models.CharField(verbose_name='交易密码',max_length=50,null=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = verbose_name_plural = '银行表'


