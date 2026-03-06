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

frontend - 127.0.0.1:8501

backend - host 127.0.0.1:9000

# Frontdend
#### Сводная статистика(page1)

##### Полный список полученных данных
![01](/imgs/01.png)

##### Выбор интервала 
![02](/imgs/02.png)

##### Блок с максимальными и минимальными значениями 
![03](/imgs/03.png)

##### Блок с графиками 
![04](/imgs/04.png)

#### Управление данными(page2)

##### Просмотр статистики
![05](/imgs/05.png)

##### Создание статистики
![06](/imgs/06.png)

##### Удаление статистики
![07](/imgs/07.png)

# Backend
Хендлеры: 
GET
POST 
PUT 
DELETE 
