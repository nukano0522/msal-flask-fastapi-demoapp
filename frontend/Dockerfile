FROM python:3.10

# 作業ディレクトリを設定
WORKDIR /app

# アプリケーションのソースコードをコピー
COPY . .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションを起動するコマンド
CMD ["python", "./frontend/app.py"]