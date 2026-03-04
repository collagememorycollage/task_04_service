import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import datetime
from streamlit_calendar import calendar 


def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("page1.py", title="Main info", icon="🔥"),
    st.Page("page2.py", title="Get statistics", icon=":material/favorite:"),
])
pg.run()



