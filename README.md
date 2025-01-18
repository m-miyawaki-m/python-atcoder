# python-atcoder


# Python AtCoder 解答＆チェック環境の構築

## プロジェクト概要
このリポジトリは、Pythonを利用してAtCoderの問題解答およびチェックを効率的に行うための環境を提供します。

### 主な機能
- **解答作成**: AtCoderの問題に対するコードを作成できます。
- **自動テスト**: サンプルテストケースを自動的に実行します。
- **提出支援**: コマンドラインを利用して簡単に提出できます。

## 環境構築

### 必要条件
- Python 3.8以上
- VSCode（Codespaces対応）
- Node.js（`atcoder-cli`用）

### Codespacesを利用したセットアップ手順
1. **リポジトリのクローン**
   Codespacesの環境でリポジトリを開きます。
   ```bash
   git clone https://github.com/m-miyawaki-m/python-atcoder.git
   cd python-atcoder
   ```

2. **仮想環境の作成**
   ```bash
   python -m venv venv
   source venv/bin/activate # Windowsの場合は venv\Scripts\activate
   ```

3. **依存ライブラリのインストール**
   ```bash
   pip install -r requirements.txt
   sudo npm install -g atcoder-cli
   ```

4. **VSCodeの設定**
   - 必要に応じて拡張機能（例: Python拡張、Code Runner）をインストール。
   - Codespaces環境で、事前に設定された開発コンテナを利用すると便利です。


# 連携確認
acc check-oj


1. ChromiumとChromeDriverのインストール
Codespaces環境でChromeDriverが正しく動作するようにします。

# bash
sudo apt-get update
sudo apt-get install -y chromium-browser chromium-chromedriver

```
machine atcoder.jp
login your_email@example.com
password your_password
```

chmod 600 ./.netrc

# login
acc login

# session確認
acc session

# online-judge-tools用ログイン
oj login https://beta.atcoder.jp/

# グローバル設定（テンプレート）
acc config default-template java
acc config default-task-choice all
acc config default-test-dirname-format tests

# acc new abc〇〇〇 --template java
#acc new abc101 --template java
acc new abc101

# configファイルの場所（config.json  session.json）
acc config-dir

acc templates
# test確認
pip install online-judge-tools
oj t -c "python main.py" -d ./tests/

# 提出
#acc submit
acc submit main.py -- --language 5055

<!-- # テスト
oj t -c "java Main.java" -d ./tests/   -->


# ディレクトリ削除
rm -rf ./abc101





## 使用方法

### 問題のダウンロード
AtCoderのコンテストURLを指定して問題を取得します。
```bash
oj dl https://atcoder.jp/contests/abc300/tasks/abc300_a
```

### コードの作成
ダウンロードされた問題フォルダ内にPythonスクリプトを作成して解答を記述します。

### テストの実行
作成した解答をサンプルケースでテストします。
```bash
oj t -c "python main.py"
```

### 提出
コードを提出します。
```bash
oj submit https://atcoder.jp/contests/abc300/tasks/abc300_a main.py
```

## ディレクトリ構造

```plaintext
.
├── main.py                # 解答スクリプト
├── requirements.txt       # 依存ライブラリ
├── .vscode/               # VSCodeの設定フォルダ
├── README.md              # 本ファイル
└── その他のファイルやディレクトリ
```

## 使用ライブラリとツール

- `tcoder-cli` - 問題管理ツール
- `online-judge-tools` - テストと提出を支援するツール
- `pytest` - テストフレームワーク（必要に応じて）

## 注意
- AtCoderの利用規約を守り、正しい方法で問題を解くよう心がけてください。
- ツールやライブラリのバージョンに依存する場合があります。公式ドキュメントを確認してください。

---
