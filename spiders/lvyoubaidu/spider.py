#!/usr/bin/python
#-*- coding=utf-8 -*-

__author__ = ['"wuyadong" <wuyadong@tigerknows.com>']

from core.spider.spider import BaseSpider
from core.datastruct import HttpTask

from spiders.lvyoubaidu.parser import (AttractionListParser,
                                       AttractionParser,
                                       CommentListParser)
from spiders.lvyoubaidu.pipeline import (AttractionItemPipeline,
                                         CommentListItemPipeline)
from spiders.lvyoubaidu.utils import (build_next_page_request,
                                      LVYOU_HOST)


class LvYouBaiDuSpider(BaseSpider):
    """抓取百度旅游的爬虫
    """
    parsers = {
        "AttractionListParser": AttractionListParser,
        "AttractionParser": AttractionParser,
        "CommentListParser": CommentListParser,
    }

    pipelines = {
        "AttractionItem": AttractionItemPipeline,
        "CommentListItem": CommentListItemPipeline,
    }

    start_tasks = [HttpTask(build_next_page_request("shanghai", 1),
                            callback="AttractionListParser",
                            max_fail_count=5, cookie_host=LVYOU_HOST)]

