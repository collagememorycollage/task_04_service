import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import datetime
from streamlit_calendar import calendar
import streamlit as st
import requests
from datetime import date
import json
from pydantic import BaseModel

class DataSchema(BaseModel):
    id: int
    timestep: str
    consumption_eur: int
    consumption_sib: int
    price_eur: float
    price_sib: float

st.title("Get stat date")

col1, col2 = st.columns(2)

with col1:
    selected_date = st.date_input("Выберите дату:", value=date(2008, 1, 1), min_value=date(2006, 9, 1), max_value=date(2011, 11, 22))
with col2:
    selected_time = st.time_input("Выберите время", value=datetime.time(12, 00), step=3600)

if selected_date or selected_time:
    req = requests.get(f'http://192.168.0.180:9000/get-date?date={selected_date} {selected_time}')
    data = req.json()
    st.write("Дата", data[0]['timestep'])
    st.write("consumption eur", data[0]['consumption_eur'])
    st.write("consumption sib", data[0]['consumption_sib'])
    st.write("Price eur", data[0]['price_eur'])
    st.write("Price sib", data[0]['price_sib'])

st.title("Create stat")
num_consumtion_eur = st.number_input("input consumption eur", min_value=0.0, format="%.5f", step=0.00001)
num_consumption_sib = st.number_input("input consumption sib", min_value=0.0, format="%.5f", step=0.00001)
num_price_eur = st.number_input("input price eur", min_value=0.0, format="%.5f", step=0.00001)
num_price_sib = st.number_input("input price sib", min_value=0.0, format="%.5f", step=0.00001)
date_create = st.date_input("Выберите дату:", value=date(2008, 1, 1))
time_create = st.time_input("Выберите время", step=60)
send_button = st.button("Отправить")

if send_button:
    data = {
        "timestep": f"{date_create.strftime('%Y-%m-%d')} {time_create.strftime('%H:%M')}",
        "consumption_eur": num_consumtion_eur,
        "consumption_sib": num_consumption_sib,
        "price_eur": num_price_eur,
        "price_sib": num_price_sib
    }
    res = requests.post('http://192.168.0.180:9000/create-data', json=data)
    st.write(data)
    st.write("Данные отправлены")
st.title("Delete stat")
col1, col2 = st.columns(2)

with col1:
    selected_date_delete = st.date_input("Выберите дату удаления:", value=date(2008, 1, 1), min_value=date(2006, 9, 1), max_value=date(2011, 11, 22))
with col2:
    selected_time_delete = st.time_input("Выберите время удаления", value=datetime.time(12, 00), step=3600)

if selected_date_delete or selected_time_delete:
    req = requests.get(f'http://192.168.0.180:9000/get-date?date={selected_date} {selected_time}')
    data = req.json()
    st.write("Дата", data[0]['timestep'])
    st.write("consumption eur", data[0]['consumption_eur'])
    st.write("consumption sib", data[0]['consumption_sib'])
    st.write("Price eur", data[0]['price_eur'])
    st.write("Price sib", data[0]['price_sib'])
    st.button("Удалить")
