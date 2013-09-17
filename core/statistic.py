#!/usr/bin/python2.7
#-*- coding=utf-8 -*-

# Copy Rights (c) Beijing TigerKnows Technology Co., Ltd.

"""
    WorkerStatistic: 用于记录worker的统计信息的类
    output_statistic_file(): 用于将统计信息输出到文件里
    output_statistic_dict(): 用于以json格式导出统计数据
"""

__authors__ = ['"wuyadong" <wuyadong@tigerknows.com>']

import datetime
import logging
from core.datastruct import Task

WORKER_STATISTIC_PATH = "data/worker_statistic.dat"
WORKER_FAIL_PATH = "data/fails/"

logger = logging.getLogger("statistic")

class WorkerStatistic(object):
    """用于统计worker的信息的类
    """

    def __init__(self):
        self._start_time = None
        self._end_time = None
        self._processing_number = 0
        self._parser2success = {}
        self._parser2fail = {}
        self._parser2retry = {}
        self._parser2fetchcount = {}
        self._parser2fetchinterval = {}
        self._parser2extractcount = {}
        self._parser2extractinterval = {}
        self._parser2handlecount = {}
        self._parser2handleinterval = {}

    @property
    def processing_number(self):
        return self._processing_number

    def incre_processing_number(self):
        """增加正在处理的个数
        """
        self._processing_number += 1

    def decre_processing_number(self):
        """减少正在处理的个数
        """
        self._processing_number -= 1

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value

    def add_spider_success(self, key_name):
        """增加某一key的成功次数
            Args：
                key_name: str, 对应的key
        """
        self._parser2success[key_name] = 1 if not self._parser2success.has_key(key_name) \
        else self._parser2success[key_name] + 1

    @property
    def parser2success(self):
        '''
        don't modify
        '''
        return self._parser2success

    def add_spider_fail(self, key_name):
        """增加对应key的失败次数
            Args:
                key_name:str,对应的key值
        """
        self._parser2fail[key_name] = 1 if not self._parser2fail.has_key(key_name) \
        else self._parser2fail.get(key_name) + 1

    @property
    def parser2fail(self):
        '''
        don't modify
        '''
        return self._parser2fail

    def add_spider_retry(self, parser_name, reason):
        if not self._parser2retry.has_key(parser_name):
            self._parser2retry[parser_name] = {}

        reason2count = self._parser2retry[parser_name]
        reason2count[reason] = 1 if not reason2count.has_key(reason) \
            else reason2count[reason] + 1

    @property
    def parser2retry(self):
        '''
        don't modify
        '''
        return self._parser2retry

    def count_average_fetch_time(self, parser_name, fetch_time, fetch_interval,
                                 default_interval=datetime.timedelta(minutes=10)):
        if not self._parser2fetchcount.has_key(parser_name):
            self._parser2fetchcount[parser_name] = {}
            self._parser2fetchinterval[parser_name] = {}

        # 更新计数器或者创建
        time2count = self._parser2fetchcount[parser_name]
        time2interval = self._parser2fetchinterval[parser_name]
        latest_fetch_time = max(time2count.keys()) if len(time2count.keys()) > 0 \
            else datetime.datetime.min
        if latest_fetch_time + default_interval < fetch_time:
            time2count[fetch_time] = 1
            time2interval[fetch_time] = fetch_interval
        else:
            time2interval[latest_fetch_time] = (time2interval[latest_fetch_time] *
                time2count[latest_fetch_time] + fetch_interval) / (time2count[latest_fetch_time] + 1)
            time2count[latest_fetch_time] += 1

    def count_average_extract_time(self, parser_name, extract_time,
            extract_interval, default_interval=datetime.timedelta(minutes=10)):
        if not self._parser2extractcount.has_key(parser_name):
            self._parser2extractcount[parser_name] = {}
            self._parser2extractinterval[parser_name] = {}

        # 更新计数器或者创建
        time2count = self._parser2extractcount[parser_name]
        time2interval = self._parser2extractinterval[parser_name]
        latest_extract_time = max(time2count.keys()) if len(time2count.keys()) > 0 \
            else datetime.datetime.min
        if latest_extract_time + default_interval < extract_time:
            time2count[extract_time] = 1
            time2interval[extract_time] = extract_interval
        else:
            time2interval[latest_extract_time] = (time2interval[latest_extract_time]
                * time2count[latest_extract_time] + extract_interval) / (time2count[latest_extract_time] + 1)
            time2count[latest_extract_time] += 1

    def count_average_handle_item_time(self, parser_name, handle_time, handle_interval,
                                    default_interval=datetime.timedelta(minutes=10)):
        if not self._parser2handlecount.has_key(parser_name):
            self._parser2handlecount[parser_name] = {}
            self._parser2handleinterval[parser_name] = {}

        # 更新计数器或者创建
        time2count = self._parser2handlecount[parser_name]
        time2interval = self._parser2handleinterval[parser_name]
        latest_handle_time = max(time2count.keys()) if len(time2count.keys()) > 0 \
            else datetime.datetime.min
        if latest_handle_time + default_interval < handle_time:
            time2count[handle_time] = 1
            time2interval[handle_time] = handle_interval
        else:
            time2interval[latest_handle_time] = (time2interval[latest_handle_time]
                * time2count[latest_handle_time] + handle_interval) / (time2count[latest_handle_time] + 1)
            time2count[latest_handle_time] += 1

    def get_average_fetch_interval(self, parser_name=""):
        '''
        don't modify
        '''
        if parser_name == "":
            return self._parser2fetchinterval
        else:
            return None if not self._parser2fetchcount.has_key(parser_name) \
                else self._parser2fetchinterval[parser_name]

    def get_average_extract_interval(self, parser_name=""):
        '''
        don't modify
        '''
        if parser_name == "":
            return self._parser2extractinterval
        else:
            return None if not self._parser2extractcount.has_key(parser_name) \
                else self._parser2extractinterval[parser_name]

    def get_average_handle_interval(self, parser_name=""):
        if parser_name == "":
            return self._parser2handleinterval
        else:
            return None if not self._parser2handleinterval.has_key(parser_name) \
                else self._parser2handleinterval[parser_name]

def output_statistic_file(file_path, work_statistic, worker_name, spider_name):
    import core.util
    with open(core.util.get_project_path() + file_path, "a") as out_file:
        out_file.write("----------------------------------%s----------------------------------------\n" % datetime.datetime.today())
        out_file.write("crawl start time: %s\n\n\n" % work_statistic.start_time)
        out_file.write("crawl end time: %s\n\n\n" % work_statistic.end_time)
        out_file.write("worker name: %s\n\n\n" % worker_name)
        out_file.write("spider name: %s\n\n\n" % spider_name)
        out_file.write("spider success count:\n")
        for key, value in work_statistic.parser2success.iteritems():
            out_file.write("%s: %s\n" % (key, value))
        out_file.write("\n\n")

        # out_file.write("spider fail count:\n")
        # for key, value in get_spider_fail().items():
        #     out_file.write("%s: %s\n" % (key, value))
        # out_file.write("\n\n")

        out_file.write("spider retry count:\n")
        for spider_name, reason2count in work_statistic.parser2retry.iteritems():
            out_file.write("%s: \n" % spider_name)
            for key, value in reason2count.iteritems():
                out_file.write("%s: %s\n" % (key, value))
            out_file.write("\n")
        out_file.write("\n\n")

        out_file.write("spider fetch interval:\n")
        for spider_name, interval_dict in work_statistic.get_average_fetch_interval().\
            iteritems():
            out_file.write("spider name: %s\n" % spider_name)
            for start_time, interval in interval_dict.iteritems():
                out_file.write("%s: %s\n" % (start_time, interval))
            out_file.write("\n")
        out_file.write("\n\n")

        out_file.write("spider extract interval:\n")
        for spider_name, interval_dict in work_statistic.get_average_extract_interval()\
            .iteritems():
            out_file.write("spider name:%s\n" % spider_name)
            for start_time, interval in interval_dict.iteritems():
                out_file.write("%s: %s\n" % (start_time, interval))
            out_file.write("\n")
        out_file.write("\n\n")

        out_file.write("spider handle item interval:\n")
        for item_name, interval_dict in work_statistic.get_average_handle_interval()\
            .iteritems():
            out_file.write("handle item name:%s\n" % item_name)
            for start_time, interval in interval_dict.iteritems():
                out_file.write("%s: %s\n" % (start_time, interval))
            out_file.write("\n")
        out_file.write("\n\n")
        out_file.write("---------------------------------------------------------------------------------------\n")


def output_statistic_dict(worker_statistic):
    statistic_dict = {}
    statistic_dict['start_time'] = None if not worker_statistic.start_time \
        else worker_statistic.start_time.strftime("%Y-%m-%d %H:%M:%S")
    statistic_dict['end_time'] = None if not worker_statistic.end_time \
        else worker_statistic.end_time.strftime("%Y-%m-%d %H:%M:%S")
    statistic_dict['success_count'] = worker_statistic.parser2success
    statistic_dict['retry_count'] = worker_statistic.parser2retry
    statistic_dict['processing_number'] = worker_statistic.processing_number

    temp_fetch_interval_dict = {}
    for parser_name, value in worker_statistic.get_average_fetch_interval().items():
        temp_dict = {}
        for start_time, interval in value.items():
            temp_dict[start_time.strftime("%Y-%m-%d %H:%M:%S")] = str(interval)
        temp_fetch_interval_dict[parser_name] = temp_dict
    statistic_dict['fetch_interval'] = temp_fetch_interval_dict

    temp_extract_interval_dict = {}
    for parser_name, value in worker_statistic.get_average_extract_interval().items():
        temp_dict = {}
        for start_time, interval in value.items():
            temp_dict[start_time.strftime("%Y-%m-%d %H:%M:%S")] = str(interval)
        temp_extract_interval_dict[parser_name] = temp_dict
    statistic_dict['extract_interval'] = temp_extract_interval_dict

    temp_handle_interval_dict = {}
    for item_name, value in worker_statistic.get_average_handle_interval().items():
        temp_dict = {}
        for start_time, interval in value.items():
            temp_dict[start_time.strftime("%Y-%m-%d %H:%M:%S")] = str(interval)
        temp_handle_interval_dict[item_name] = temp_dict
    statistic_dict['item_interval'] = temp_handle_interval_dict

    return statistic_dict


def output_fail_task_file(file_path, schedule):
    """output all fail task to file

        notice:N_Line

        Args:
            file_path: str, file path to store fail task
            schedule: Schedule, schedule for spider
    """
    import core.util
    with open(core.util.get_project_path() + file_path, "w") as out_file:
        for task in schedule.dumps_all_fail_task():
            line = '"%s" "%s"\n' % (task.callback, task.request.url)
            out_file.write(line)
