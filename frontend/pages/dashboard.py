import streamlit as st

from frontend.api_client import request


st.title("📊 Dashboard")

ok, tasks = request("GET", "/tasks")
if not ok:
    st.error(f"Could not load tasks: {tasks}")
    st.stop()

ok, summary = request("GET", "/stats/reward-available")
if not ok:
    st.error(f"Could not load statistics: {summary}")
    st.stop()

if not tasks:
    st.info("Add some tasks to see statistics.")
    st.stop()

total = len(tasks)
completed = sum(1 for task in tasks if task["completed"])
completion_rate = completed / total

with st.container(border=True):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("All tasks", total)
    c2.metric("Completed", completed)
    c3.metric("Open", summary["open_tasks"])
    c4.metric("Available rewards", f'{summary["available_reward"]:.0f} RON')
    st.progress(completion_rate, text=f"{completion_rate:.0%} completed")

by_language = {}
by_difficulty = {}
for task in tasks:
    by_language[task["language"]] = by_language.get(task["language"], 0) + 1
    by_difficulty[task["difficulty"]] = by_difficulty.get(task["difficulty"], 0) + 1

c1, c2 = st.columns(2)
with c1:
    st.subheader("Tasks by language")
    st.bar_chart(by_language)
with c2:
    st.subheader("Tasks by difficulty")
    st.bar_chart(by_difficulty)

open_tasks = sorted(
    (task for task in tasks if not task["completed"]),
    key=lambda task: task["reward"],
    reverse=True,
)[:5]

st.subheader("Most valuable open tasks")
if open_tasks:
    st.dataframe(
        [
            {
                "Title": task["title"],
                "Language": task["language"],
                "Difficulty": task["difficulty"],
                "Reward": task["reward"],
            }
            for task in open_tasks
        ],
        use_container_width=True,
        hide_index=True,
    )
else:
    st.success("All tasks are completed.")
