#!/bin/bash
PWD=$(pwd)
echo $PWD

echo "🧹 Очистка портов 9000 и 8501..."
kill -9 $(lsof -t -i:8501)
kill -9 $(lsof -t -i:9000)

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "✅ Окружение .venv создано."
else
    echo "ℹ️ Окружение .venv уже существует."
fi

source .venv/bin/activate

pip install -r requirements.txt

echo "🚀 Окружение готово и активировано!"

uvicorn backend.main:app --host 127.0.0.1 --port 9000  &

python -m streamlit run frontend/main.py  --server.address 127.0.0.1 --server.port 8501 &




