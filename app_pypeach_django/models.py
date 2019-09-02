from django.db import models


class Employees(models.Model):
    emp_no = models.IntegerField('社員番号')
    department_no = models.IntegerField('部署')
    first_name = models.CharField('姓', max_length=30)
    last_name = models.CharField('名', max_length=30)
    gender = models.IntegerField('性別')
    birth_date = models.CharField('誕生日', max_length=8)
    hire_date = models.CharField('退社日', max_length=8)
    department_date_from = models.CharField('配属開始日', max_length=8)
    department_date_to = models.CharField('配属終了日', max_length=8, null=True)
    delete_flag = models.IntegerField('削除フラグ')
    regist_dt = models.DateTimeField('登録日時', auto_now_add=True)
    update_dt = models.DateTimeField('更新日時', auto_now_add=True)

    class Meta:
        db_table = 'employees'
        verbose_name = '社員情報'
        unique_together = ('emp_no',)


class Departments(models.Model):
    department_no = models.IntegerField('部署番号')
    department_name = models.CharField('部署名', max_length=30)
    delete_flag = models.IntegerField('削除フラグ')
    regist_dt = models.DateTimeField('登録日時', auto_now_add=True)
    update_dt = models.DateTimeField('更新日時', auto_now_add=True)

    class Meta:
        db_table = 'departments'
        verbose_name = '配属情報'


class ScrapyHtml(models.Model):
    execute_dt = models.CharField('実行日', max_length=8)
    request_url = models.CharField('リクエストURL', max_length=256)
    html_text = models.TextField('HTMLテキスト')
    delete_flag = models.IntegerField('削除フラグ')
    regist_dt = models.DateTimeField('登録日時', auto_now_add=True)
    update_dt = models.DateTimeField('更新日時', auto_now_add=True)

    class Meta:
        db_table = 'scrapy_html'
        verbose_name = 'WebスクレイピングHTML'
