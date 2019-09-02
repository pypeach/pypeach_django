from django.db import transaction, connection
from django.utils import timezone
from django.utils.timezone import localtime

from app_pypeach_django.application.enums.department_type import DepartmentType
from app_pypeach_django.application.enums.gender_type import GenderType
from app_pypeach_django.application.service.app_logic_base import AppLogicBaseService
from app_pypeach_django.models import Employees, Departments

"""
employeesテーブルを操作するクラスです。
"""
__author__ = "t.ebinuma"
__version__ = "1.0"
__date__ = "02 September 2019"


class EmployeesService(AppLogicBaseService):
    def __init__(self):
        super().__init__()

    @staticmethod
    @transaction.atomic()
    def create_employees():
        """
        Employeesを作成する
        """
        service = EmployeesService()

        for emp_no in range(1, 11):
            if Employees.objects.filter(emp_no=emp_no, delete_flag=0).count() == 0:
                if emp_no <= 5:
                    department_no = DepartmentType.SALES.value
                else:
                    department_no = DepartmentType.MARKETING.value

                # データを登録する
                service._regist_employees(department_no, emp_no)

    @staticmethod
    @transaction.atomic()
    def create_departments():
        """
        Departmentsを作成する
        """
        service = EmployeesService()

        for department_type in DepartmentType:
            department_no = department_type.value
            if Departments.objects.filter(department_no=department_no, delete_flag=0).count() == 0:
                # データを登録する
                service._regist_departments(department_no, department_type.en_name)

    @staticmethod
    @transaction.atomic()
    def update_employees():
        """
        Employeesを更新する
        """
        service = EmployeesService()

        # filterによる絞込を行う
        # gt:...より大きい(>),lt:...より小さい(<)になる
        for item_employees in Employees.objects.filter(emp_no__gt=1, emp_no__lt=3, delete_flag=0):
            employees_id = item_employees.id
            department_no = DepartmentType.PRODUCTION.value
            department_date_from = 20190903
            # データを更新する
            service._update_employees_department(employees_id, department_no, department_date_from)

        # filterによる絞込を行う
        # gte:...以上(>=),lte:...以下(<=)になる
        for item_employees in Employees.objects.filter(emp_no__gte=7, emp_no__lte=9, delete_flag=0):
            employees_id = item_employees.id
            department_no = DepartmentType.SALES.value
            department_date_from = 20190905
            # データを更新する
            service._update_employees_department(employees_id, department_no, department_date_from)

    @staticmethod
    @transaction.atomic()
    def truncate_employees():
        """
        トランケートを行う
        """
        cursor = connection.cursor()
        cursor.execute('TRUNCATE TABLE {0}'.format(Employees._meta.db_table))

    def _regist_employees(self, department_no, emp_no):
        """
        employeesを登録する
        """
        self.regist_model = Employees()
        self.regist_model.emp_no = emp_no
        self.regist_model.department_no = department_no
        self.regist_model.gender = GenderType.MAN.value
        self.regist_model.department_date_from = "20190902"
        self.regist_model.delete_flag = 0
        self.regist_model.regist_dt = localtime(timezone.now())
        self.regist_model.update_dt = localtime(timezone.now())
        self.regist_model.save()
        return self.regist_model.id

    def _regist_departments(self, department_no, department_name):
        """
        departmentsを登録する
        """
        self.regist_model = Departments()
        self.regist_model.department_no = department_no
        self.regist_model.department_name = department_name
        self.regist_model.delete_flag = 0
        self.regist_model.regist_dt = localtime(timezone.now())
        self.regist_model.update_dt = localtime(timezone.now())
        self.regist_model.save()

    def _update_employees_department(self, employees_id, department_no, department_date_from):
        """
        配属情報を更新する
        """
        self.update_model = Employees()
        self.update_model.pk = employees_id
        self.update_model.department_no = department_no
        self.update_model.department_date_from = department_date_from
        self.update_model.update_dt = localtime(timezone.now())
        self.update_model.save(update_fields=['department_no', 'department_date_from', 'update_dt'])
