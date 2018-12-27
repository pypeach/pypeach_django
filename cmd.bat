@echo off
if %1%==mi (
  rem マイグレーションを行う
  python manage.py makemigrations
  python manage.py migrate
) else if %1%==me (
  rem メッセージファイルをコンパイルする
  django-admin compilemessages -l ja
) else if %1%==idb (
  rem DB定義のモデルをテキストファイルに出力する
  python manage.py inspectdb > inspectdb_list.txt
) else (
  rem コマンド失敗
  echo error command
)
