# -*- coding: utf-8 -*-
__author__ = "hulinjun"

from django import template
from datetime import datetime
register = template.Library()


@register.simple_tag
def active_tag():
    """
    设置哪个导航的tag是当前活动的
    :return:
    """
    return 10

@register.simple_tag
def now_data():
    """
    当前时间
    :return:
    """
    return datetime.today().strftime('%Y{0}%m{1}%d{2}').format('年','月','日')


@register.filter
def format_time(value):
    """
    "北京时间 11:05:39" 格式化成"11:05:39"
    :param value:
    :return:
    """
    return value.split(' ')[1]