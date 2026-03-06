import streamlit as st
from streamlit_calendar import calendar

pg = st.navigation([
    st.Page("page1.py", title="Сводная статистика", icon="🔥"),
    st.Page("page2.py", title="Управление данными", icon=":material/favorite:"),
])

pg.run()


