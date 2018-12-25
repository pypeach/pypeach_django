@echo off
if %1%==mi (
  python manage.py makemigrations
  python manage.py migrate
) else if %1%==me (
  django-admin compilemessages -l ja
) else if %1%==idb (
  python manage.py inspectdb > inspectdb_list.txt
) else (
  echo error command
)
