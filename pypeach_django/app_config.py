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


def get_properties(key):
    """
    設定ファイルからキーに紐づく値を取得する
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resource_file = base_dir + "/resource/application_" + get_application_config() + ".yml"

    with open(os.path.join(resource_file), 'r', encoding='UTF-8') as f:
        config = f.read()
    return yaml.load(config)[key]


def get_log_file():
    """
    設定ファイルからキーに紐づく値を取得する
    """
    return os.path.join(get_properties("log_path"), get_properties("log_file"))


def get_application_config():
    """
    ホスト名から設定ファイルの読み込み先を取得する
    """
    application_config = "develop"

    if socket.gethostname() == 'example.com':
        application_config = "production"
    return application_config


def get_logging_level_config():
    """
    ホスト名からログレベルを取得する
    """
    logging_level = "DEBUG"
    if socket.gethostname() == 'example.com':
        logging_level = "INFO"

    return logging_level
