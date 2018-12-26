#!/bin/sh

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$HOME/.pyenv/shims:$HOME/.pyenv/bin:$PATH"
LANG=ja_JP.UTF-8

export PYTHONPATH="$HOME/pypeach_django/"

python /home/pypeach/pypeach_django/manage.py batch_main $1 $2

exit 0
