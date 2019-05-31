import logging

from app_pypeach_django.application.helper.string import StringHelper
from app_pypeach_django.test.test_base import UnitTestBase

"""
文字列ユーティリティのテストです
"""
__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "25 December 2018"


class TestStringHelper(UnitTestBase):

    def test_convert_string_to_float_001(self):
        """
        文字列→数値(float)変換を検証するテストケースです
        """
        self.assertEqual(StringHelper.convert_string_to_float("4.0"), 4.0)
        self.assertEqual(StringHelper.convert_string_to_float("4"), 4.0)
        self.assertEqual(StringHelper.convert_string_to_float("4.05"), 4.05)
        self.assertEqual(StringHelper.convert_string_to_float("4.00001"), 4.00001)
        self.assertEqual(StringHelper.convert_string_to_float("0"), 0)
        self.assertEqual(StringHelper.convert_string_to_float("-1.0"), -1.0)
        self.assertNotEqual(StringHelper.convert_string_to_float("1.0"), 1.1)

    def test_convert_string_to_float_002(self):
        """
        文字列→数値(float)変換を検証(異常)するテストケースです
        """
        # 無効な文字列を指定する
        with self.assertRaises(ValueError):
            StringHelper.convert_string_to_float("a")

    def test_convert_string_to_int_001(self):
        """
        文字列→数値(int)変換を検証するテストケースです
        """
        self.assertEqual(StringHelper.convert_string_to_int("4"), 4)
        self.assertEqual(StringHelper.convert_string_to_int("0"), 0)
        self.assertEqual(StringHelper.convert_string_to_int("-1"), -1)

    def test_convert_string_to_date_002(self):
        """
        文字列→数値(int)変換を検証(異常)するテストケースです
        """
        with self.assertRaises(ValueError):
            StringHelper.convert_string_to_int("a")

    def test_re_space_001(self):
        """
        空白文字の除去を検証するテストケースです
        """
        line = ' 　example-  　example  　 '
        logging.debug(StringHelper.re_space(line))
        self.assertEqual(StringHelper.re_space(line), "example-example")
        self.assertEqual(len(StringHelper.re_space(line)), 15)
