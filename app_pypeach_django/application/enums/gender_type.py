from enum import Enum

from django.utils.translation import gettext

"""
性別のEnum
"""

__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "25 December 2018"


class GenderType(Enum):
    MAN = 1
    WOMAN = 2
    UNKNOWN = 9
