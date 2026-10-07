import streamlit as st

from frontend.api_client import request


st.title("➕ Add a task")

with st.form("add-task"):
    title = st.text_input("Title", placeholder="Build a reporting endpoint")
    language = st.selectbox("Language", ["Python", "JavaScript", "Go", "Rust"])
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"])
    reward = st.number_input("Reward (RON)", min_value=1.0, step=10.0)
    submitted = st.form_submit_button("Create task", type="primary")

if submitted:
    payload = {
        "title": title,
        "language": language,
        "difficulty": difficulty,
        "reward": reward,
    }
    ok, result = request("POST", "/tasks", json=payload)
    if ok:
        st.success(f'Task “{result["title"]}” was created.')
    else:
        st.error(result)
