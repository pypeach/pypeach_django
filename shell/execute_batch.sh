#!/bin/sh

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$HOME/.pyenv/shims:$HOME/.pyenv/bin:$PATH"
LANG=ja_JP.UTF-8

export PYTHONPATH="$HOME/pypeach_django/"

python $PYTHONPATH/manage.py batch_main $1

exit 0
