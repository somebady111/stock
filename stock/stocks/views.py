# Create your views here.
# -*- coding:utf-8 -*-
__author__ = 'Tony Qu'
from django.http import HttpResponse,HttpRequest
# from userinfo.models import *
from deal.models import *
# from sqlalchemy import create_engine
from .data import  *
import json
import decimal
import time
from django.core import serializers
## This example upgrade by Tony Qu in 2018
## It includes some basic function about search a car or
## a part of car in some known_car
## PLEASE NOTE:
## If you have trouble installing it, try any of the other demos
## that don't require it instead.
# from .models import *
# import logging

# Create your views here.
# code,代码
# name,名称
# industry,所属行业
# area,地区
# pe,市盈率
# outstanding,流通股本(亿)
# totals,总股本(亿)
# totalAssets,总资产(万)
# liquidAssets,流动资产
# fixedAssets,固定资产
# reserved,公积金
# reservedPerShare,每股公积金
# esp,每股收益
# bvps,每股净资
# pb,市净率
# timeToMarket,上市日期
# undp,未分利润
# perundp, 每股未分配
# rev,收入同比(%)
# profit,利润同比(%)
# gpr,毛利率(%)
# npr,净利润率(%)
# holders,股东人数
# 首页数据
# imglist = [
#     "./files/152325746135108262.jpg",
#     "./files/152325801935026945.jpg",
#     "./files/152325764192299701.jpg",
#     "./files/152325955961408523.jpg",
#     "./files/152325996596110237.jpg",
#     "./files/153308810955203407.jpg",
#     "./files/153310814123886653.jpg",
#     "./files/153732615261934581.jpg",
#     "./files/152325975175681529.jpg",
#     "./files/152334871285296849.jpg",
#     "./files/152325744368242911.jpg",
#     "./files/152669706937044832.jpg",
#     "./files/152325792390298426.jpg",
#     "./files/152325804328282570.jpg",
#     "./files/152325797085141352.jpg",
#     "./files/152325782634688466.jpg",
#     "./files/152325790116109401.jpg",
#     "./files/152384413173813127.jpg",
#     "./files/152325962565387782.jpg",
#     "./files/152325760428408141.jpg",
# ]

imglist = [
    "./static/files/152325746135108262.jpg",
    "./static/files/152325801935026945.jpg",
    "./static/files/152325764192299701.jpg",
    "./static/files/152325955961408523.jpg",
    "./static/files/152325996596110237.jpg",
    "./static/files/153308810955203407.jpg",
    "./static/files/153310814123886653.jpg",
    "./static/files/153732615261934581.jpg",
    "./static/files/152325975175681529.jpg",
    "./static/files/152334871285296849.jpg",
    "./static/files/152325744368242911.jpg",
    "./static/files/152669706937044832.jpg",
    "./static/files/152325792390298426.jpg",
    "./static/files/152325804328282570.jpg",
    "./static/files/152325797085141352.jpg",
    "./static/files/152325782634688466.jpg",
    "./static/files/152325790116109401.jpg",
    "./static/files/152384413173813127.jpg",
    "./static/files/152325962565387782.jpg",
    "./static/files/152325760428408141.jpg",
]


def index(request):

    if request.method == "GET":
        print("%%%%%%%%%%%%%%%%%%%")
        data = {}
        # 股票列表
        stocklist = []
        stock_data = stock_all_data(None)[0:20]
        # print(stock_data)
        # stockpl = []
        # for index,idx in enumerate(stock_data.index):
        #     # print(type(idx))
        #     # print(type(stock_data.ix[idx]['name']))
        #     stockpl.append(Stock(stonumber=idx, company_name=stock_data.ix[idx]['name'],
        #                            industry=stock_data.ix[idx]['industry'],area=stock_data.ix[idx]['area'],
        #                            pe=decimal.Decimal(stock_data.ix[idx]['pe']), outstanding=decimal.Decimal(stock_data.ix[idx]['outstanding']),
        #                            totals=decimal.Decimal(stock_data.ix[idx]['totals']), totalAssets=decimal.Decimal(stock_data.ix[idx]['totalAssets']),
        #                            liquidAssets=decimal.Decimal(stock_data.ix[idx]['liquidAssets']), fixedAssets=decimal.Decimal(stock_data.ix[idx]['fixedAssets']),
        #                            reserved=decimal.Decimal(stock_data.ix[idx]['reserved']), reservedPerShare=decimal.Decimal(stock_data.ix[idx]['reservedPerShare']),
        #                            bvps=decimal.Decimal(stock_data.ix[idx]['bvps']), pb=decimal.Decimal(stock_data.ix[idx]['pb']),
        #                            timeToMarket=stock_data.ix[idx]['timeToMarket']))
        # for i in stockpl:
        #     print(type(i))
        # print(type(stockpl))
        # Stock.objects.bulk_create(stockpl)
        for index,idx in enumerate(stock_data.index):
            stocko = {}
            stocko['code'] = idx
            stocko['name'] = stock_data.ix[idx]['name']
            # 市盈率
            stocko['pe'] = stock_data.ix[idx]['pe']
            stocko['img'] = imglist[index]
            stocklist.append(stocko)
        dealstocks = DealStock.objects.all()
        if len(dealstocks) >= 10:
            dealstocks = dealstocks[0:0:-1]
            dealstocks = dealstocks[0:10]
        else:
            dealstocks = dealstocks[0:len(dealstocks)]
        dealstockshow = []
        for dealstock in dealstocks:
            a = {}
            a['price'] = str(dealstock.price)
            a['amount'] = dealstock.amount
            a['datetime'] = dealstock.get_datetime()
            a['stock'] = dealstock.stock
            dealstockshow.append(a)
        data['stocklist'] = stocklist
        data['dealstocks'] = dealstockshow
        return HttpResponse(json.dumps({"result": True, "data": data, "error": ""}))


# k线数据
def k_data(request):
    code = request.GET.get('code')
    data = {}
    datas = {}
    # k线图
    k_data = stock_k_data(code)
    datastr = []
    for idx in k_data.index:
        rowlist = []
        rowlist.append(idx)
        rowlist.append(k_data.ix[idx]['open'])
        rowlist.append(k_data.ix[idx]['close'])
        rowlist.append(k_data.ix[idx]['low'])
        rowlist.append(k_data.ix[idx]['high'])
        rowlist.append(k_data.ix[idx]['volume'])
        datastr.append(rowlist)
    data['datastr'] = datastr[::-1]

    # 股票头
    # 1：open，今日开盘价
    # 2：pre_close，昨日收盘价
    # 3：price，当前价格
    # 4：high，今日最高价
    # 5：low，今日最低价
    # 8：volume，成交量
    # 9：amount，成交金额（元
    # CNY）
    stockdata = {}
    stock_now = stock_now_all(code)
    name = stock_now.name
    price = "%.2f" % (float(stock_now.price[0]))
    open_price = "%.2f"%(float(stock_now.open[0]))
    high = "%.2f"%(float(stock_now.high[0]))
    low = "%.2f"%(float(stock_now.low[0]))
    pre_close = "%.2f"%(float(stock_now.pre_close[0]))
    volume = "%.2f"%(float(stock_now.volume[0]) / 100000000)
    amount = "%.2f"%(float(stock_now.amount[0]) / 100000000)
    change = "%.2f"%(float(price) - float(pre_close))
    perce = "%.2f"%(float(change) / float(pre_close) * 100)
    stockdata['name'] = str(name[0])
    stockdata['price'] = price
    stockdata['open_price'] = open_price
    stockdata['high'] = high
    stockdata['low'] = low
    stockdata['pre_close'] = pre_close
    stockdata['volume'] = volume
    stockdata['amount'] = amount
    stockdata['change'] = change
    stockdata['perce'] = perce
    data['stockdata'] = stockdata
    #深度图,买卖各六个
    stockdeeps = []
    bosstockb = BOSStock.objects.filter(stock__stonumber=code, role=0)
    print(bosstockb)
    if len(bosstockb) >= 4:
        # bosstockb = bosstockb[::-1]
        bosstock = bosstockb[0:4]
    else:
        bosstock = bosstockb[0:len(bosstockb)]
    for bos in bosstock:
        stockdeep = {}
        stockdeep['role'] = bos.get_role()
        stockdeep['price'] = str(bos.price)
        stockdeep['amount'] = bos.amount
        stockdeep['datetime'] = bos.get_datetime()
        stockdeeps.append(stockdeep)
    bosstocksa = BOSStock.objects.filter(stock__stonumber=code, role=1)
    if len(bosstocksa) >= 4:
        # bosstockb = bosstockb[::-1]
        bosstock = bosstocksa[0:4]
    else:
        bosstock = bosstocksa[0:len(bosstocksa)]
    for bos in bosstock:
        stockdeep = {}
        stockdeep['role'] = bos.get_role()
        stockdeep['price'] = str(bos.price)
        stockdeep['amount'] = bos.amount
        stockdeep['datetime'] = bos.get_datetime()
        stockdeeps.append(stockdeep)
    data['stockdeep'] = stockdeeps
    return HttpResponse(json.dumps({"result": True, "data": data, "error": ""}))




#
#
# #头部数据调用
# def realHead(request,template):
#     if template == 'index':
#         df = stock_A()
#     else:
#         df = stock_company(template)
#     price = "%.2f"%(float(df.price[0]))
#     open_price = "%.2f"%(float(df.open[0]))
#     high = "%.2f"%(float(df.high[0]))
#     low = "%.2f"%(float(df.low[0]))
#     pre_close = "%.2f"%(float(df.pre_close[0]))
#     volume = "%.2f"%(float(df.volume[0]) / 100000000)
#     amount = "%.2f"%(float(df.amount[0]) / 100000000)
#     change = "%.2f"%(float(price) - float(pre_close))
#     perce = "%.2f"%(float(change) / float(pre_close) * 100)
#     return render(request,'realHead.html',locals())
#
#
# # 热点资讯
# def hotInfo(request):
#     news = stock_news()[:8]
#     news_title = serializers.serialize('json', news.title)
#     return HttpResponse(news_title)
#
#
# # 指数排行
# def indexRang(request):
#     index = stock_index()[:8]
#     a =zip(index.name,index.change)
#     b = []
#     for i in a:
#         c={}
#         c['name'] = i[0]
#         c['change'] = i[1]
#         b.append(c)
#     return HttpResponse(json.dumps(b))
#
#
# # 实时解盘
# def breakUp(request):
#     bread_up = stock_breakup()[:5]
#     # print(type(bread_up))
#     ba = zip(bread_up.title, bread_up.time, bread_up.url)
#     bb = []
#     for i in ba:
#         bc={}
#         bc['title'] = i[0]
#         bc['time'] = i[1]
#         bc['url'] = i[2]
#         bb.append(bc)
#     return HttpResponse(json.dumps(bb))
#
#
# # 自选股
# def selfStock(request, stockNo):
#     user = UserInfo.objects.filter(id=request.user.id)
#     if len(user) > 0:
#         stock = Stock.objects.filter(number=stockNo)
#         SelfStock.objects.create(user=user[0].id, stock=stock[0].id)
#         try:
#             selfstock = SelfStock.objects.filter(user_id=request.user.id)
#             if len(selfstock) > 0:
#                 data = serializers.serialize(selfstock)
#                 return HttpResponse(json.dumps({"result": False, "data": data, "error": ""}))
#             else:
#                 return HttpResponse(json.dumps({"result": False, "data": "", "error": "该用户尚未添加自选股"}))
#         except BaseException as e:
#             logging.warning(e)
#     else:
#         return HttpResponse(json.dumps({"result":False, "data":"", "error":"去登录"}))
