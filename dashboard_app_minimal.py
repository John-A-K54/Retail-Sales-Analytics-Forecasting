import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout='wide', page_title='Retail Analytics - Minimal')

st.title('Retail Analytics & Forecasting - Minimal Submission')

@st.cache_data
def load_data():
    df = pd.read_csv('/mnt/data/capstone_outputs/processed_sales_minimal.csv')
    return df

df = load_data()

st.header('Overview')
col1, col2, col3 = st.columns(3)
col1.metric('Total Sales', f"{df['Total_Sales'].sum():,.0f}")
col2.metric('Total Units', f"{df['Units_Sold'].sum():,.0f}")
col3.metric('Unique Stores', df['Store_ID'].nunique())

st.header('Forecast (next 30 days)')
fc = pd.read_csv('/mnt/data/capstone_outputs/forecast_next_30_days.csv')
st.line_chart(fc.set_index('Date')['forecast'])

st.header('Store Segmentation Sample')
seg = pd.read_csv('/mnt/data/capstone_outputs/store_segmentation.csv')
st.dataframe(seg.head(20))
