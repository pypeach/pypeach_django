import logging

from app_pypeach_django.application.helper.scrapy_helper import ScrapyHelper, HttpErrorException, ScrapyIllegalException
from app_pypeach_django.test.test_base import UnitTestBase

"""
scrapyのテストです
"""
__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "31 January 2019"


class TestScrapyHelper(UnitTestBase):

    def test_get_html_001(self):
        """
        htmlの取得を検証するテストケースです
        """
        html = ScrapyHelper.get_html('http://mocjax.com/example/scrape/', True)
        logging.debug("html={}".format(html))

        self.assertEqual(len(html.findAll('div')), 14)
        self.assertEqual(len(html.findAll('h1')), 4)

    def test_get_html_002(self):
        """
        htmlの取得(異常)を検証するテストケースです
        """
        # 存在しないURL(404)を指定する
        with self.assertRaises(HttpErrorException):
            ScrapyHelper.get_html('http://mocjax.com/example/scrape2/')

        # 誤ったURL指定になっている
        with self.assertRaises(ScrapyIllegalException):
            ScrapyHelper.get_html('//mocjax.com/pypeach/pypeach-example/example.html')
        with self.assertRaises(ScrapyIllegalException):
            ScrapyHelper.get_html('http//example.com')
        with self.assertRaises(ScrapyIllegalException):
            ScrapyHelper.get_html('http//192.168.10.10')

    def test_is_exists_class_name_001(self):
        """
        html内のclass有無を検証するテストケースです
        """
        html = ScrapyHelper.get_html('http://mocjax.com/example/scrape/', True)
        logging.debug("html={}".format(html))

        self.assertEqual(ScrapyHelper.is_exists_class_name(html, 'btn-lg'), True)
        self.assertEqual(ScrapyHelper.is_exists_class_name(html, 'jumbotron'), True)
        self.assertEqual(ScrapyHelper.is_exists_class_name(html, 'flex-column'), True)
        self.assertEqual(ScrapyHelper.is_exists_class_name(html, 'jumbotron_01'), False)
