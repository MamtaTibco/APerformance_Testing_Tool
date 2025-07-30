# components/sidebar.py
import streamlit as st
import json
import os
from datetime import datetime
from collections import OrderedDict


def group_history_by_date(history_data):
    """
    Returns an OrderedDict grouped by date label:
    {
        'Jul 15': [(entry, index), ...],
        'Jul 14, 2024': [(entry, index), ...],
        ...
    }
    """
    grouped = OrderedDict()
    for idx, entry in enumerate(history_data):
        try:
            dt = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")
        except Exception:
            dt = datetime.now()

        label = dt.strftime("%b %d")
        if dt.year != datetime.now().year:
            label += f", {dt.year}"

        grouped.setdefault(label, []).append((entry, idx))
    return grouped


def render_sidebar():
    st.sidebar.header("🕘 Request History")
    history_file = "history_tibcoresponse.json"

    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []

        grouped = group_history_by_date(history)

        for date_label, items in grouped.items():
            with st.sidebar.expander(f"📅 {date_label} ({len(items)})", expanded=True):
                for item, idx in items:
                    col1, col2 = st.columns([0.85, 0.15])

                    # Replay button
                    with col1:
                        time_only = item.get("timestamp", "").split(" ")[1]
                        btn_label = f"{item['method']} {item['url']} ({time_only})"
                        if st.button(btn_label, key=f"req_{idx}"):
                            st.session_state["selected_request"] = item
                            st.subheader("🔁 Replaying Previous Request")
                            st.json(item)

                    # Delete button
                    with col2:
                        if st.button("🗑️", key=f"del_{idx}", help="Delete this request"):
                            del history[idx]
                            with open(history_file, "w") as f:
                                json.dump(history, f, indent=2)
                            st.rerun()
