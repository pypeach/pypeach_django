# pypeach_django
## はじめに
djangoを使用してバッチ処理を行うサンプルアプリケーションです。  

### 前提事項
サンプルアプリケーションの動作環境は以下となります。
windows及びlinux(Ubuntu 18.04 LTS)で動作確認しています。  

|  項目 | バージョン |
|:------------|:------------|
| python | 3.6.3 |
| mysql | 5.6.40 |



## プロジェクト構成
プロジェクト構成は以下となります。  
djangoプロジェクトのデフォルトに一部リソースのフォルダを追加しました。 

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
  ├─template  
  └─.gitignore等  
  
```

|  項目 | 説明 |
|:------------|:------------|
| app_pypeach_django | アプリケーションのパッケージ |
| log| ログ出力先のフォルダ |
| locale| getTextで使用するメッセージを格納するフォルダ |
| pypeach_django| django関連の設定を定義するフォルダ |
| resources| 設定ファイルを格納するフォルダ |
| template| テンプレートファイル（メールテンプレート等）を格納するフォルダ |

## セットアップ
サンプルアプリケーションのセットアップを行います。 

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
| Jenkins | 「[JenkinsのフロントにApache httpdを立たせてプロキシ連携させる設定方法](https://weblabo.oscasierra.net/jenkins-apache-httpd-proxy/)」参照 |

### モジュールのインストール
pythonのモジュールはpipで適宜インストールを行います。

|  モジュール | 用途 |
|:------------|:------------|
| Django | フレームワーク |
| lxml＆yaml | 設定ファイルの読込等 |
| mysqlclient | mysqlドライバ |


テキスト(freezeで作成)を使用して以下のコマンドでインストールできます。
```
# pipコマンドを実行する
pip install -r requirements.txt

# txtの中身は以下になります
beautifulsoup4==4.6.0
Django==2.1
django-admin-tools==0.8.1
django-bootstrap-form==3.3
lxml==4.0.0
mysqlclient==1.3.12
PyYAML==3.12
```

### DB作成
mysqlのDBやユーザを作成します。
```
# DBを作成する
CREATE DATABASE pypeach_django;
# ユーザを作成する
CREATE USER 'pypeach_django'@'localhost' IDENTIFIED BY 'pypeach_django';
# DBにユーザ権限を付与する
GRANT ALL ON pypeach_django.* TO 'pypeach_django'@'localhost';
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
gettextを使用するためのメッセージを作成します。

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
例）C:\pypeach_django\manage.py batch_main test_service
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
例）python /home/pypeach_django/manage.py batch_main test_service

# linuxの場合、shellコマンドを使用できるようにしました
{プロジェクトのホーム}/shell/execute_batch.sh {起動パラメータ}
例） /home/pypeach_django/shell/execute_batch.sh test_service
```

djangoTestは以下のように実行します。
```
# 環境変数を設定する
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$HOME/.pyenv/shims:$HOME/.pyenv/bin:$PATH"
LANG=ja_JP.UTF-8
export PYTHONPATH="$HOME/pypeach_django/"
# testを実行する
python {プロジェクトのホーム}/manage.py test --keepdb {テストクラス}
例）python /home/pypeach_django/manage.py test --keepdb app_pypeach_django.test.test_date_helper
```
