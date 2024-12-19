FROM python:3.10

# 作業ディレクトリを設定
WORKDIR /app

# ソースコードをコピー
COPY . .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# Uvicornを使ってアプリケーションを起動するコマンド
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]