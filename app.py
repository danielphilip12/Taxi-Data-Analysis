import streamlit as st
import pandas as pd

st.title("Taxi Data Analysis")


about_page = st.Page(
    "st_templates/about.py",
    title="About me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    "st_templates/dashboard.py", title="Taxi Dashboard", icon=":material/bar_chart:"
)

# --- Navigation Session Setup ---
pn = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page],
    }
)

# Stuff to share with all pages
# st.logo('./assets/logo.png')
st.sidebar.markdown("Thank you for comming to my Ted Talk!")

# --- Running Navigation ---
pn.run()

