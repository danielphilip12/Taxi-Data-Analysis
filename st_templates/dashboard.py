import streamlit as st
import pandas as pd

DATA = "https://raw.githubusercontent.com/danielphilip12/Taxi-Data-Analysis/refs/heads/main/data/cleaned_taxi.csv"

df = pd.read_csv(DATA).assign(
    pickup=lambda df: pd.to_datetime(df['pickup']),
    dropoff=lambda df: pd.to_datetime(df['dropoff'])
)

boroughs = df['dropoff_borough'].unique()
# st.write(boroughs)

st.title("Dashboard of NYC Taxi")

st.write("Subset of data")
st.dataframe(df.sample(10, random_state=42), hide_index=True)

st.markdown("## Revenue by Dropoff Location (Borough)")

borough_sales = (
    df.groupby(['dropoff_borough'])['total']
    .sum()
)

columns = st.columns(5)
for i,borough in enumerate(boroughs):
    with columns[i]:
        st.metric(
            label=borough,
            value=f"$ {borough_sales.loc[borough]:,.0f}"
        )
        
selected_borough = st.selectbox(
    label='Select Borough',
    options=boroughs
)

filtered_data = (
    df.query('dropoff_borough == @selected_borough')
    .groupby('dropoff_zone', dropna=False)['total']
    .sum()
    .reset_index()
)

show_dataframe = st.toggle(
    value=False, label='Show Borough Data'
)

if show_dataframe == True:
    st.dataframe(filtered_data)

st.bar_chart(filtered_data.set_index(filtered_data.columns[0])['total'])