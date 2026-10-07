import streamlit as st

from frontend.api_client import request


st.title("📋 Tasks")

ok, tasks = request("GET", "/tasks")
if not ok:
    st.error(f"Could not connect to the API: {tasks}")
    st.stop()

if not tasks:
    st.info("No tasks yet. Add the first one from the sidebar.")
    st.stop()

for task in tasks:
    with st.container(border=True):
        left, middle, right = st.columns([4, 2, 2])
        left.subheader(task["title"])
        left.caption(f'{task["language"]} · {task["difficulty"]}')
        middle.metric("Reward", f'{task["reward"]:.0f} RON')

        if task["completed"]:
            right.success("Completed")
        elif right.button("Mark complete", key=f'complete-{task["id"]}'):
            success, result = request("PUT", f'/tasks/{task["id"]}/complete')
            if success:
                st.rerun()
            st.error(result)

        if st.button("Delete", key=f'delete-{task["id"]}', type="secondary"):
            success, result = request("DELETE", f'/tasks/{task["id"]}')
            if success:
                st.rerun()
            st.error(result)
