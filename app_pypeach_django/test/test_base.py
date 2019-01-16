import filecmp
import os

from django.test import TestCase

"""
テストクラスの基底クラスです。TestCaseを継承します
"""
__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "25 December 2018"


class UnitTestBase(TestCase):

    def assert_file_exists(self, file_path):
        """
        ファイルが存在することをチェックする
        """
        self.assertTrue(os.path.isfile(file_path))

    def assert_file_not_exists(self, file_path):
        """
        ファイルが存在しないことをチェックする
        """
        self.assertFalse(os.path.isfile(file_path))

    def assert_file_empty(self, file_path):
        """
        ファイルが0バイトであることをチェックする
        """
        self.assertEqual(os.path.getsize(file_path), 0)

    def assert_file_not_empty(self, file_path):
        """
        ファイルが0バイトでないことをチェックする
        """
        self.assertGreater(os.path.getsize(file_path), 0)

    def assert_file_equals(self, actual_file_path, expected_file_path):
        """
        指定された2ファイルの内容が正しいかチェックする
        """
        self.assertTrue(filecmp.cmp(actual_file_path, expected_file_path))

    def assert_file_not_equals(self, actual_file_path, expected_file_path):
        """
        指定された2ファイルの内容が異なるかチェックする
        """
        self.assertFalse(filecmp.cmp(actual_file_path, expected_file_path))
