# ベースとなるDockerイメージを指定
FROM python:3.11.1

# 作業ディレクトリを設定
WORKDIR /venv_design_search

# ホストのrequirements.txtをコンテナの作業ディレクトリにコピー
COPY requirements.txt .

# requirements.txtに基づいて依存関係をインストール
RUN pip install -r requirements.txt

# Djangoのバージョンを指定してインストール
RUN pip install django==4.2.4

# ホストのカレントディレクトリの内容をコンテナの作業ディレクトリにコピー
COPY . .

# Djangoアプリケーションを実行
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
