#!/bin/bash
PWD=$(pwd)
echo $PWD

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

python -m streamlit run frontend/main.py &


