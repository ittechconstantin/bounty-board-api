import streamlit as st

st.set_page_config(page_title="Bounty Board", page_icon="🧩", layout="wide")

pagina_lista = st.Page("s38_pages/lista.py", title="Task-uri", icon="📋", default=True)
pagina_adauga = st.Page("s38_pages/adauga.py", title="Adauga task", icon="➕")
pagina_dashboard = st.Page("s38_pages/dashboard.py", title="Dashboard", icon="📊")

navigare = st.navigation([pagina_lista, pagina_adauga, pagina_dashboard])
navigare.run()
