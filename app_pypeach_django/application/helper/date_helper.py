# coding:utf-8
import datetime

"""
日付関連の共通処理を定義する
"""

__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "28 April 2018"


class DateHelper:
    # 日付フォーマット:ymd
    format_ymd = '%Y%m%d'
    # 日付フォーマット:hm
    format_hm = '%H%M'
    # 日付フォーマット:ymd_hm
    format_ymd_hm = '%Y%m%d%H%M'
    # 日付フォーマット:ymd_hms
    format_ymd_hms = '%Y%m%d%H%M%S'

    @staticmethod
    def get_date_list(days_interval, sort_flag=False):
        """
        今日から指定された過去日までの日付リストを取得する
        """
        date_list = []
        for i in range(0, days_interval):
            d = datetime.date.today() - datetime.timedelta(days=i)
            date_list.append('%02d%02d%02d' % (d.year, d.month, d.day))

        if sort_flag is True:
            date_list.sort()
        return date_list

    @staticmethod
    def get_today(formatter):
        """
        現在年月日時を取得する
        """
        now = datetime.datetime.now()
        return now.strftime(formatter)

    @staticmethod
    def get_before_minute(datetime_string, minutes_interval, formatter):
        """
        過去年月日時間(分指定)を取得する
        """
        dt_tm = datetime.datetime.strptime(datetime_string, formatter)
        before_minute = dt_tm - datetime.timedelta(minutes=minutes_interval)
        return before_minute.strftime(formatter)

    @staticmethod
    def get_before_today(days_interval, formatter):
        """
        過去年月日時間(日指定)を取得する
        """
        dt_tm = datetime.datetime.strptime(DateHelper.get_today(formatter), formatter)
        before_day = dt_tm - datetime.timedelta(days=days_interval)
        return before_day.strftime(formatter)
