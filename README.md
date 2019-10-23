# pypeach_django
## はじめに
djangoを使用してバッチ処理を行うサンプルアプリケーションです。  

### 前提事項
サンプルアプリケーションの動作環境は以下となります。
windows及びlinux(Ubuntu 18.04 LTS)で動作確認しています。  

|  項目 | バージョン |
|:------------|:------------|
| python | 3.7.3 |
| mysql | 5.7.27 |



## プロジェクト構成
プロジェクト構成は以下となります。  
djangoプロジェクトのデフォルトに設定ファイル関連のディレクトリを追加しました。 

```
/$  
  ├─app_pypeach_django
  │  ├─management
  │  │  └─commands
  │  └─migrations
  ├─locale
  ├─log
  ├─pypeach_django
  ├─resources
  ├─shell  
  ├─template  
  └─.gitignore等  
  
```

|  項目 | 説明 |
|:------------|:------------|
| app_pypeach_django | アプリケーションのパッケージ |
| log| ログ出力先のフォルダ |
| locale| getTextで使用するメッセージを格納するディレクトリ |
| pypeach_django| django関連の設定を定義するディレクトリ |
| resources| 設定ファイルを格納するディレクトリ |
| shell| 起動シェルスクリプトを格納するディレクトリ |
| template| テンプレートファイル（メールテンプレート等）を格納するディレクトリ |

## セットアップ
サンプルアプリケーションのセットアップを行います。 
Ansibleを使用したセットアップは[Gitリポジトリ](https://github.com/pypeach/pypeach_playbook.git)を参照ください。

### Gitリポジトリのクローン
サンプルアプリケーションは[Gitリポジトリ](https://github.com/pypeach/pypeach_django.git)からクローンしてください。  

### ソフトウェアのインストール
python等のソフトウェアを適宜インストールしてください。  
以下を参考にしました。  

|  項目 | 説明 |
|:------------|:------------|
| Vagrant + VirtualBox | 「[Vagrant + VirtualBoxでWindows上に開発環境をサクッと構築する](https://qiita.com/ozawan/items/160728f7c6b10c73b97e)」参照 |
| Vagrant(DNS設定)| 「[VagrantのゲストOSから名前解決できない件](https://saku.io/fix-dns-resolver-in-vagrant-vm/)」参照 |
| python | 「[Python3.6.0をUbuntu16.04に導入する](https://qiita.com/Fendo181/items/912b65c4fcc3d701d53d)」参照 |
| Jenkins | 「[Ubuntu 12.04にJenkinsをインストールしてApacheでポート80で動かす](http://madroom-project.blogspot.com/2012/12/ubuntu-1204jenkinsapache80.html)」参照 |
| mysql(mysqlclient) | 「[【MySQL入門】PythonからMySQLを使ってみよう！mysqlclient利用編](https://www.sejuku.net/blog/82657)」参照 |
| virtualenv | 「[venvを用いてプロジェクトごとに独立した環境を構築する](https://www.yoheim.net/blog.php?q=20171106)」参照 |

### モジュールのインストール
pythonのモジュールはpipで適宜インストールを行います。
|  モジュール | 用途 |
|:------------|:------------|
| Django | フレームワーク |
| lxml＆yaml | 設定ファイルの読込等 |
| mysqlclient | mysqlドライバ |
| pytest | unittest |
| beautiful soup | Webスクレイピング |

テキスト(freezeで作成)を使用して以下のコマンドでインストールできます。
```
# pipコマンドを実行する
pip install -r requirements.txt

# requirements.txtの内容は以下になります
atomicwrites==1.2.1
attrs==18.2.0
beautifulsoup4==4.6.0
coverage==4.5.2
Django==2.1.5
django-admin-tools==0.8.1
django-bootstrap-form==3.4
lxml==4.3.0
more-itertools==5.0.0
mysqlclient==1.4.2
pluggy==0.8.1
py==1.7.0
pytest==4.1.1
pytest-cov==2.6.1
pytest-django==3.4.5
pytz==2018.9
PyYAML==3.12
six==1.12.0
unittest-xml-reporting==2.2.1

```

### DB作成
mysqlのDBやユーザを作成します。
```
# DBを作成する
CREATE DATABASE pypeach CHARACTER SET utf8mb4;
CREATE DATABASE test_pypeach CHARACTER SET utf8mb4;
# ユーザを作成する
CREATE USER 'pypeach'@'localhost' IDENTIFIED BY 'pypeach';
# DBにユーザ権限を付与する
GRANT ALL ON pypeach.* TO 'pypeach'@'localhost';
GRANT ALL ON test_pypeach.* TO 'pypeach'@'localhost';
# 権限変更を反映する
FLUSH PRIVILEGES;
```

djangoを使用するためのテーブルも合わせて作成します。

```
# マイグレーションを行う
python manage.py makemigrations
python manage.py migrate

# windowsの場合、batコマンドを使用できるようにしました
{プロジェクトのホーム}\cmd mi
例）C:\pypeach_django\cmd mi

```

### メッセージ作成
[gettext](https://www.howtoinstall.co/en/ubuntu/xenial/gettext)を使用するためのメッセージを作成します。

```
# poファイルを作成する
django-admin compilemessages -l ja

# windowsの場合、batコマンドを使用できるようにしました
{プロジェクトのホーム}\cmd me
例）C:\pypeach_django\cmd me
```

## サンプルアプリケーション実行
環境変数を設定してサンプルアプリケーションを実行します。  
【windowsの場合】
```
# 環境変数を設定する
set PYTHONPATH={プロジェクトのホーム}
# アプリケーションを実行する
python {プロジェクトのホーム}\manage.py batch_main {起動パラメータ}
例）C:\pypeach_django\manage.py batch_main create_employees
```
【linux/macの場合】
```
# 環境変数を設定する
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$HOME/.pyenv/shims:$HOME/.pyenv/bin:$PATH"
LANG=ja_JP.UTF-8
export PYTHONPATH="$HOME/pypeach_django/"
# アプリケーションを実行する
python {プロジェクトのホーム}/manage.py batch_main {起動パラメータ}
例）python /home/pypeach/pypeach_django/manage.py batch_main create_employees

# linuxの場合、shellコマンドを使用できるようにしました
{プロジェクトのホーム}/shell/execute_batch.sh {起動パラメータ}
例） /home/pypeach/pypeach_django/shell/execute_batch.sh create_employees
```

djangoTestは以下のように実行します。
```
# 環境変数を設定する
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$HOME/.pyenv/shims:$HOME/.pyenv/bin:$PATH"
LANG=ja_JP.UTF-8
export PYTHONPATH="$HOME/pypeach_django/"
# testを実行する。DB定義を保持するため"--keepdb"のオプションを指定する
python {プロジェクトのホーム}/manage.py test --keepdb {テストクラス}
例）python /home/pypeach/pypeach_django/manage.py test --keepdb app_pypeach_django.test.test_date

# pytestを実行する(プロジェクトのホームで実行する)
pytest --ds={プロジェクトの設定} --reuse-db --junitxml={テスト結果のxmlファイル名} {テスト対象パッケージ}
例）pytest --ds=pypeach_django.settings --reuse-db --junitxml=unittest.xml app_pypeach_django/test

```
