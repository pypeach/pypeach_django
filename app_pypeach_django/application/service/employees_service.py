from django.db import transaction, connection
from django.utils import timezone
from django.utils.timezone import localtime

from app_pypeach_django.application.enums.gender_type import GenderType
from app_pypeach_django.application.service.app_logic_base_service import AppLogicBaseService
from app_pypeach_django.models import Employees

"""
employeesテーブルを操作するクラスです。
"""
__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "25 December 2018"


class EmployeesService(AppLogicBaseService):
    def __init__(self):
        super().__init__()

    @staticmethod
    @transaction.atomic()
    def create_employees():
        """
        employeesに存在しないデータを作成する
        """
        service = EmployeesService()
        for emp_no in range(1, 7):
            if Employees.objects.filter(emp_no=emp_no, delete_flag=0).count() == 0:
                service._regist_employees(emp_no)

    @staticmethod
    @transaction.atomic()
    def truncate_employees():
        """
        employeesをトランケートする
        """
        cursor = connection.cursor()
        cursor.execute('TRUNCATE TABLE {0}'.format(Employees._meta.db_table))

    def _regist_employees(self, emp_no):
        """
        employeesを登録する
        """
        self.regist_model = Employees()
        self.regist_model.emp_no = emp_no
        self.regist_model.gender = GenderType.MAN.value
        self.regist_model.delete_flag = 0
        self.regist_model.regist_dt = localtime(timezone.now())
        self.regist_model.update_dt = localtime(timezone.now())
        self.regist_model.save()
        return self.regist_model.id
