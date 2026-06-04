import streamlit as st

st.title(
    "Scenario Analysis"
)

scenario = st.selectbox(
    "Scenario",
    [
        "TP Rate Revision",
        "EV Growth",
        "Monsoon Catastrophe"
    ]
)

st.write(
    f"Selected: {scenario}"
)
