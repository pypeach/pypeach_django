import logging

from app_pypeach_django.application.helper.date_helper import DateHelper
from app_pypeach_django.test.test_base import UnitTestBase

"""
日付ユーティリティのテストです
"""
__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "25 December 2018"


class TestDateHelper(UnitTestBase):

    def test_get_date_list_001(self):
        """
        日付リスト取得を検証するテストケースです
        """
        logging.debug("date_list={}".format(DateHelper.get_date_list(7)))
        logging.debug("date_list_sort={}".format(DateHelper.get_date_list(7, True)))

        self.assertEqual(len(DateHelper.get_date_list(7)), 7)
        self.assertEqual(len(DateHelper.get_date_list(7, True)), 7)

    def test_get_today_dt_tm_001(self):
        """
        現在年月日時の取得を検証するテストケースです
        """
        logging.debug("today_dt_tm={}".format(DateHelper.get_today("%Y/%m/%d %H:%M:%S")))

        self.assertEqual(len(DateHelper.get_today('%Y%m%d')), 8)
        self.assertEqual(len(DateHelper.get_today('%Y/%m/%d')), 10)

    def test_get_before_minute_dt_tm_001(self):
        """
        過去年月日時間(分指定)を検証するテストケースです
        """
        self.assertEqual(DateHelper.get_before_minute("201812221649", 1, DateHelper.format_ymd_hm),
                         "201812221648")
        self.assertEqual(DateHelper.get_before_minute("201812221640", 50, DateHelper.format_ymd_hm),
                         "201812221550")
        self.assertEqual(DateHelper.get_before_minute("20181222164030", 5, DateHelper.format_ymd_hms),
                         "20181222163530")

    def test_get_before_minute_dt_tm_002(self):
        """
        過去年月日時間(分指定)を検証(異常)するテストケースです
        """
        # 文字列を値に指定する
        with self.assertRaises(ValueError):
            DateHelper.get_before_minute("test", 5, DateHelper.format_ymd_hms)

    def test_get_before_today_001(self):
        """
        過去年月日の取得を検証するテストケースです
        """
        logging.debug("dt={}".format(DateHelper.get_before_today(1, DateHelper.format_ymd)))

        self.assertEqual(len(DateHelper.get_before_today(1, DateHelper.format_ymd)), 8)
