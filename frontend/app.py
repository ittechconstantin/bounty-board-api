import streamlit as st


st.set_page_config(page_title="Bounty Board", page_icon="🧩", layout="wide")

pages = [
    st.Page("pages/tasks.py", title="Tasks", icon="📋", default=True),
    st.Page("pages/add_task.py", title="Add task", icon="➕"),
    st.Page("pages/dashboard.py", title="Dashboard", icon="📊"),
]

navigation = st.navigation(pages)
navigation.run()
