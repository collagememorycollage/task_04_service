import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import datetime
from streamlit_calendar import calendar
import streamlit as st
import requests
from datetime import date
from pydantic import BaseModel

SERVER_HOST = "http://127.0.0.1"
SERVER_PORT = "9000"
MIN_DATE = date(2006, 9, 1)
MAX_DATE = date(2011, 11, 22)
DEFAULT_DATE = date(2008, 1, 1)
DEFAULT_TIME = datetime.time(12, 00)

class DataSchema(BaseModel):
    id: int
    timestep: str
    consumption_eur: int
    consumption_sib: int
    price_eur: float
    price_sib: float

def fetch_data(endpoint, method=None, **kwargs):
    url = f"{SERVER_HOST}:{SERVER_PORT}/{endpoint.lstrip('/')}"
    try:
        if method == "POST":
            res = requests.post(url, json=data)
        elif method == "DELETE":
            res = requests.delete(url) # Обычно ID уже в endpoint
        else:
            res = requests.get(url)

        res.raise_for_status() 
        return res.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        st.error(f"Не удалось получить данные: {e}")
        return None


def display_records(data):
    if isinstance(data, list) and len(data) > 0:
        item = data[0]
        print(data[0])
        st.divider()
        col1, col2 = st.columns(2)
        st.metric("Дата", item.get('timestep', 'Н/Д'))
        with col1:
            st.metric("ID", item.get('id'))
            st.metric("Потребление EUR", item.get('consumption_eur', 0))
            st.metric("Потребление SIB", item.get('consumption_sib', 0))
        with col2:
            st.metric("Цена EUR", item.get('price_eur', 0))
            st.metric("Цена SIB", item.get('price_sib', 0))
        st.divider()
        return item
    st.warning("Данные не найдены")
    return None

st.title("🔍 Просмотр статистики")
col1, col2 = st.columns(2)
with col1:
    selected_date = st.date_input("Дата:", value=DEFAULT_DATE, min_value=MIN_DATE, max_value=MAX_DATE)
with col2:
    selected_time = st.time_input("Время", value=DEFAULT_TIME, step=3600)

if st.button("Найти запись"):
	res_data = fetch_data(f'get-date?date={selected_date} {selected_time}', 'GET')
	display_records(res_data)


st.title("➕ Создание статистики")

with st.form("create_form"):
    num_consumtion_eur = st.number_input("input consumption eur", min_value=0.0, format="%.5f", step=0.00001)
    num_consumption_sib = st.number_input("input consumption sib", min_value=0.0, format="%.5f", step=0.00001)
    num_price_eur = st.number_input("input price eur", min_value=0.0, format="%.5f", step=0.00001)
    num_price_sib = st.number_input("input price sib", min_value=0.0, format="%.5f", step=0.00001)
    date_create = st.date_input("Выберите дату:", value=date(2008, 1, 1))
    time_create = st.time_input("Выберите время", step=60)
    send_button = st.form_submit_button("Отправить")

if send_button:
    data = {
        "timestep": f"{date_create.strftime('%Y-%m-%d')} {time_create.strftime('%H:%M')}",
        "consumption_eur": num_consumtion_eur,
        "consumption_sib": num_consumption_sib,
        "price_eur": num_price_eur,
        "price_sib": num_price_sib
    }
    
    res_data = fetch_data(f"/create-data", "POST", json=data)
    st.write("Данные отправлены")


st.title("🗑️ Удаление статистики")
select_id = st.number_input("Введите ID", step=1)

if st.button("Удалить"):
    try:
        res_data = fetch_data(f"delete-data/{select_id}", "DELETE")
        st.write("Запись успешно удалена")
    except Exception as e:
        st.error("Записи с таким ID не существует")
#             
