import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import datetime
from streamlit_calendar import calendar
import streamlit as st


df = pd.read_csv("./../backend/data.csv")


df['timestep'] = pd.to_datetime(df['timestep'])


date = datetime.datetime.now().strftime("%d, %B, %Y")
st.title(f"Time: {date}")


# 2. Виджет выбора диапазона
dates = st.date_input(
    "Выберите диапазон дат",
    value=(df['timestep'].min(), df['timestep'].max()),
    min_value=df['timestep'].min(),
    max_value=df['timestep'].max()
)

# 3. Фильтрация (проверка, что выбраны обе даты: начало и конец)
if isinstance(dates, tuple) and len(dates) == 2:
    start_date, end_date = dates
    
    # Преобразуем границы из date в datetime, чтобы сравнение работало
    start_dt = pd.to_datetime(start_date)
    # Конец дня, чтобы захватить данные за последнюю выбранную дату целиком
    end_dt = pd.to_datetime(end_date) + pd.Timedelta(hours=23, minutes=59, seconds=59)
    
    # Фильтруем (теперь типы слева и справа совпадают)
    mask = (df['timestep'] >= start_dt) & (df['timestep'] <= end_dt)
    filtered_df = df.loc[mask]
   
    col1, col2 = st.columns(2)

    #max min
    with col1:

        max_price_eur = filtered_df['price_eur'].max()
        st.write("Max price eur: ", max_price_eur)


        max_price_sib = filtered_df['price_sib'].max()
        st.write("Max price sib: ", max_price_sib)

    with col2:
    
        max_consumption_eur = filtered_df['consumption_eur'].max()
        st.write("Max consumption eur: ", max_consumption_eur)


        max_consumption_sib = filtered_df['consumption_sib'].max()
        st.write("Max consumption sib: ", max_consumption_sib)


    #fig_1
    st.title("consumption EUR")
    fig1 = px.bar(filtered_df, x='timestep', y='consumption_eur')
    st.plotly_chart(fig1, width='stretch')
    #fig_2
    st.title("price EUR")
    fig2 = px.bar(filtered_df, x='timestep', y='price_eur')
    st.plotly_chart(fig2, width='stretch')
    #fig_3
    st.title("consumption SIB")
    fig3 = px.bar(filtered_df, x='timestep', y='consumption_sib')
    st.plotly_chart(fig3, width='stretch')
    #fig_4
    st.title("price SIB")
    fig4 = px.bar(filtered_df, x='timestep', y='price_sib')
    st.plotly_chart(fig4,width='stretch')
else:
    st.info("Выберите конечную дату диапазона")

