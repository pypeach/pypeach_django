from django.db import models


class Employees(models.Model):
    emp_no = models.IntegerField('社員番号')
    first_name = models.CharField('姓', max_length=30)
    last_name = models.CharField('名', max_length=30)
    gender = models.IntegerField('性別')
    birth_date = models.CharField('誕生日', max_length=8)
    hire_date = models.CharField('退社日', max_length=8)
    delete_flag = models.IntegerField('削除フラグ')
    regist_dt = models.DateTimeField('登録日時', auto_now_add=True)
    update_dt = models.DateTimeField('更新日時', auto_now_add=True)

    class Meta:
        db_table = 'employees'
        verbose_name = '社員情報'
        unique_together = ('emp_no',)
