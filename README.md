# 📊 Energy Data Pipeline & Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Сервис для мониторинга и анализа данных энергопотребления (EUR/SIB). Система включает в себя REST API на бэкенде и интерактивный дашборд для визуализации метрик.

## 📂 Структура проекта

```text
task_04_service/
├── backend/            # Серверная часть (API)
│   ├── main.py         # Логика FastAPI и обработка данных
│   └── data.csv        # Источник данных (временные ряды)
├── frontend/           # Клиентская часть (Dashboard)
│   ├── main.py         # Основной запуск Streamlit
│   ├── page1.py        # Визуализация и графики
│   └── page2.py        # Управление данными (CRUD)
├── .gitignore          # Исключение лишних файлов (.venv, __pycache__)
├── README.md           # Документация проекта
├── requirements.txt    # Список всех библиотек
└── start.sh            # Скрипт для одновременного запуска сервисов
```


## 🛠 Архитектура
- **Frontend**: Streamlit (мультистраничное приложение).
- **Backend**: FastAPI (Uvicorn сервер).
- **Storage**: CSV-based хранилище данных.

## 📦 Установка и запуск

Скачивание проекта 
```
git clone https://github.com/collagememorycollage/task_04_service
```
Даем права доступа
```
chmod -R 777 task_04_service
```
Переходим в дерикторию
```
cd task_04_service
```
Запускаем скрипт для старта проекта
```
./start.sh
```

frontend -
backend -

# Frontdend
#### Сводная статистика
#### Управление данными

# Backend
Хендлеры: 
GET
POST 
PUT 
DELETE 
