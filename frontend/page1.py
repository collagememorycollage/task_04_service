import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import datetime
from streamlit_calendar import calendar
import streamlit as st
import requests
import json

SERVER_HOST = "http://127.0.0.1"
SERVER_PORT = "9000"
DATE = datetime.datetime.now().strftime("%d, %B, %Y")
DATA = None

st.title(f"Дата: {DATE}")

def fetch_data():
    try:
        res = requests.get(f"{SERVER_HOST}:{SERVER_PORT}/get-all-data")
        df = pd.DataFrame(res.json())
        st.title("Полный список полученных данных")
        df['timestep'] = pd.to_datetime(df['timestep'])
        st.write(df)
        return df

    except Exception as e:
        st.error(f"Ошибка подключения к серверу {e}")
        return None

def draw_max(df):
    st.subheader("Максимальные показатели за период")
    m_cols = st.columns(4)
    metrics = [
        ("Цена EUR", "price_eur", "€"),
        ("Цена SIB", "price_sib", "₽"),
        ("Потребление EUR", "consumption_eur", "kW"),
        ("Потребление SIB", "consumption_sib", "kW")
    ]

    for col, (label, field, unit) in zip(m_cols, metrics):
        val = df[field].max()
        col.metric(label, f"{val:.2f} {unit}")

def draw_min(df):
    st.subheader("Максимальные показатели за период")
    m_cols = st.columns(4)
    metrics = [
        ("Цена EUR", "price_eur", "€"),
        ("Цена SIB", "price_sib", "₽"),
        ("Потребление EUR", "consumption_eur", "kW"),
        ("Потребление SIB", "consumption_sib", "kW")
    ]

    for col, (label, field, unit) in zip(m_cols, metrics):
        val = df[field].min()
        col.metric(label, f"{val:.2f} {unit}")

def draw_graph(df):
    print(df.info())
    plots = [
        ("Потребление EUR", "consumption_eur", "teal"),
        ("Цена EUR", "price_eur", "gold"),
        ("Потребление SIB", "consumption_sib", "blue"),
        ("Цена SIB", "price_sib", "orange")
    ]

    dates = st.date_input(
        "Выберите диапазон дат",
        value=('2008-01-10', '2008-10-10'),
        min_value=df['timestep'].min(),
        max_value=df['timestep'].max()
    )

    start_date, end_date = dates
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date)
    mask = (df['timestep'] >= start_dt) & (df['timestep'] <= end_dt)
    filtered_df = df.loc[mask]

    draw_min(filtered_df)
    draw_max(filtered_df)

    st.divider()
    chart_cols = st.columns(2)

    chart_cols = st.columns(2)

    for i, (title, column, color) in enumerate(plots):
        with chart_cols[i % 2]:
            fig = px.bar(
                filtered_df,
                x='timestep',
                y=column,
                title=title,
                color_discrete_sequence=[color]
            )
            fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig, use_container_width=True)

DATA = fetch_data()
draw_graph(DATA)
