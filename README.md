# pypeach_django
## はじめに
djangoのサンプルアプリケーションです。  

### 前提事項
サンプルアプリケーションの動作環境は以下となります。
windows及びlinux(CentOS7.2)で動作確認しています。  

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
| python | 「[CentOSにPythonをインストールする](https://qiita.com/micheleno13/items/bd19dca20da97f3f056e)」参照 |
| pip | 「[CentOS7 に pip と awscli をインストール](http://rriifftt.hatenablog.com/entry/2015/10/28/142043)」参照 |
| Jenkins | 「[JenkinsのフロントにApache httpdを立たせてプロキシ連携させる設定方法](https://weblabo.oscasierra.net/jenkins-apache-httpd-proxy/)」参照 |

### モジュールのインストール
pythonのモジュールはpipで適宜インストールを行います。

|  モジュール | 用途 |
|:------------|:------------|
| Django |フレームワーク |
| lxml/yaml |設定ファイルの読込等 |
| mysqlclient  | mysqlドライバー |

freezeで出力したテキスト(requirements.txt)を使用して以下のコマンドでインストールできます。
```
# pipコマンドを実行する
pip install -r requirements.txt
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
