# coding:utf-8
import os
import socket

import yaml

"""
アプリケーションの設定を制御する
"""
__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "25 December 2018"


class AppConfig:

    @staticmethod
    def get_properties(key):
        """
        設定ファイルからキーに紐づく値を取得する
        """
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        resource_file = base_dir + "/resource/application_" + AppConfig.get_application_config() + ".yml"

        with open(os.path.join(resource_file), 'r', encoding='UTF-8') as f:
            config = f.read()
        return yaml.load(config)[key]

    @staticmethod
    def get_log_file():
        """
        設定ファイルからキーに紐づく値を取得する
        """
        return os.path.join(AppConfig.get_properties("log_path"), AppConfig.get_properties("log_file"))

    @staticmethod
    def get_application_config():
        """
        OS情報やホスト名から設定ファイルの読み込み先を取得する
        """
        application_config = "develop"

        # 実行環境に応じて設定ファイルの読み込み先を切り替える
        # Linux またはホスト名で判定しています
        if os.name == 'posix' or socket.gethostname() == 'example.com':
            application_config = "production"
        return application_config
