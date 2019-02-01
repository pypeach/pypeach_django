import gettext
import logging

from django.core.management.base import BaseCommand
from django.db import ProgrammingError
from django.utils.translation import gettext

from app_pypeach_django.application.service.employees_service import EmployeesService
from app_pypeach_django.application.service.scrapy_service import ScrapyService

"""
BaseCommandを継承したバッチ起動クラスです。
"""
__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "25 December 2018"


class Command(BaseCommand):

    def add_arguments(self, parser):
        """
        引数をセットする
        """
        parser.add_argument('parameter', nargs='+', type=str)

    def handle(self, *args, **options):
        """
        コマンド実行時のハンドラ。
        引数に応じて各サービスを実行する
        """
        execute_batch = None

        for index, parameter in enumerate(options['parameter']):
            if index == 0:
                execute_batch = parameter

        logging.info(gettext("I900"), execute_batch)

        try:
            if execute_batch == 'create_employees':
                EmployeesService.create_employees()
            elif execute_batch == 'create_scrapy_html':
                ScrapyService.create_scrapy_html()
            elif execute_batch == 'parse_scrapy_html':
                ScrapyService.parse_scrapy_html()
            else:
                logging.info(gettext("E902"), execute_batch)
        except ProgrammingError as e:
            logging.exception(gettext("E903"), e)
        except Exception as e:
            logging.exception(gettext("E990"), e)

        logging.info(gettext("I901"), execute_batch)
