# 📊 Energy Data Pipeline & Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Сервис для мониторинга и анализа данных энергопотребления (EUR/SIB). Система включает в себя REST API на бэкенде и интерактивный дашборд для визуализации метрик.

## 📂 Структура проекта
task_04_service/
│
├── backend/                   
│   ├── data.csv         
│   └── main.py       
├── frontend/                    
│   ├── main.py   
│   ├── page1.py
│   └── page2.py
├── .gitignore        
├── README.md 
├── requirements.txt
└── start.sh

## 🛠 Архитектура
- **Frontend**: Streamlit (мультистраничное приложение).
- **Backend**: FastAPI (Uvicorn сервер).
- **Storage**: CSV-based хранилище данных.

## 📦 Установка и запуск

Для запуска проекта 
```
git clone https://github.com/collagememorycollage/task_04_service
chmod -R 777 task_04_service
cd task_04_service
./start.sh
```
После чего будут установлены зависимости и файла requirements.txt и развернуто 2 сервера. 

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
