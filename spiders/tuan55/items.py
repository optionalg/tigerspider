#!/usr/bin/python2.7
#-*- coding=utf-8 -*-

# Copy Rights (c) Beijing TigerKnows Technology Co., Ltd.

"""描述窝窝团购中提取出的结果的定义
    CityItem: 存储城市信息的类
    DealItem: 存储团购信息的类
    WebItem: 网页解析结果的类
"""

__author__ = ['"wuyadong" <wuyadong@tigerknows.com>']

from core.datastruct import Item

class CityItem(Item):
    """城市信息类
    """
    def __init__(self, chinese_name, english_name, city_code):
        """初始化函数
            Args:
                chinese_name: str, 中文名
                english_name: str, 英文名字
                city_code: str, city代码
        """
        self.city_code = city_code
        self.chinese_name = chinese_name
        self.english_name = english_name

class DealItem(Item):
    """团购信息类
    """

    def __init__(self, price, city_code, dealid, url, name, discount_type, start_time,
                 end_time, discount, original_price, noticed, pictures, description,
                 deadline, short_desc, content_text, content_pic, purchased_number,
                 m_url, appointment, place, save, remaining, limit, refund):
        """初始化函数
            Args:
                略
        """
        self.save = save
        self.remaining = remaining
        self.limit = limit
        self.refund = refund
        self.price = price
        self.city_code = city_code
        self.dealid = dealid
        self.url = url
        self.name = name
        self.discount_type = discount_type
        self.start_time = start_time
        self.end_time = end_time
        self.discount = discount
        self.original_price = original_price
        self.noticed = noticed
        self.pictures = pictures
        self.description = description
        self.deadline = deadline
        self.short_desc = short_desc
        self.content_text = content_text
        self.content_pic = content_pic
        self.purchased_number = purchased_number
        self.m_url = m_url
        self.appointment = appointment
        self.place = place

class WebItem(Item):
    """用于保存解析网页结果的item
    """
    def __init__(self, name, noticed, description, short_desc, content_text, content_pic,
                 refund, save, place, deadline, discount_type):
        """初始化函数
            Args:
                略
        """
        self.deadline = deadline
        self.name = name
        self.noticed = noticed
        self.description = description
        self.short_desc = short_desc
        self.content_text = content_text
        self.content_pic = content_pic
        self.refund = refund
        self.place = place
        self.save = save
        self.discount_type = discount_type

class PictureItem(Item):
    """用于保存图片信息的item
    """
    def __init__(self, picture, path):
        """初始化函数
            Args:
                picture: 二进制，图片内容
                path: str, 图片路径
        """
        self.picture = picture
        self.path = path