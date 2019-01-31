"""
Scrapyを行うクラスです。
"""
import logging

from bs4 import BeautifulSoup
from django.db import transaction
from django.utils import timezone
from django.utils.timezone import localtime

from app_pypeach_django.application.helper.date_helper import DateHelper
from app_pypeach_django.application.helper.scrapy_helper import ScrapyHelper
from app_pypeach_django.application.service.app_logic_base_service import AppLogicBaseService
from app_pypeach_django.models import ScrapyHtml

__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "31 January 2019"


class ScrapyService(AppLogicBaseService):
    def __init__(self):
        super().__init__()

    # URLの定数
    url = 'http://mocjax.com/example/scrape/'

    @staticmethod
    @transaction.atomic()
    def scrapy_html():
        """
        Webページにアクセスしてデータを作成する
        """
        service = ScrapyService()
        service._regist_scrapy_html(service.url)

    @staticmethod
    @transaction.atomic()
    def validate_html():
        """
        Webページの結果から要素を抽出する
        """
        service = ScrapyService()

        for item_scrapy_html in ScrapyHtml.objects.filter(request_url=service.url, delete_flag=0):
            # html→lxmlに変換して構文解析を行う
            html_text = item_scrapy_html.html_text
            html_lxml = BeautifulSoup(html_text, 'lxml')
            # headingをすべて抽出する
            for item_header in html_lxml.select('div.card-header > h4'):
                logging.debug("header_text={}".format(item_header.text))

            # body内のタイトルを先頭1件のみ抽出する
            first_body = html_lxml.select_one('div.card-body > h1')
            logging.debug("item_header_text={}".format(first_body.text))

            # ボタンのクラス有無を判定する
            if ScrapyHelper.is_exists_class_name(html_lxml.select_one('a.btn.btn-primary'), 'btn-lg'):
                logging.debug("exists class:btn-lg")

    def _regist_scrapy_html(self, url):
        """
        Webスクレイピングした結果をテーブルに登録する
        """
        # 同一URLが存在する場合はレコードを削除する
        if ScrapyHtml.objects.filter(request_url=url).count() > 0:
            ScrapyHtml.objects.filter(request_url=url).delete()
        self.regist_model = ScrapyHtml()
        self.regist_model.execute_dt = DateHelper.get_today(DateHelper.format_ymd)
        self.regist_model.request_url = url
        self.regist_model.html_text = ScrapyHelper.get_html(url)
        self.regist_model.delete_flag = 0
        self.regist_model.regist_dt = localtime(timezone.now())
        self.regist_model.update_dt = localtime(timezone.now())
        self.regist_model.save()
        return self.regist_model.id
