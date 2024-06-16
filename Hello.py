import pandas as pd
import yfinance as yf
import streamlit as st
import datetime


st.header('Stock market analysis')
ticker_symbol = st.text_input("Stock Analysis", "MSFT",key='Placeholder')

col1, col2 = st.columns(2)

with col1:
   Startdate = st.date_input("START TIME", datetime.date(2019, 1, 1))

with col2:
   enddate = st.date_input("End time", datetime.date(2024, 5, 30))


ticker_data= yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="1d",start=Startdate,end=enddate)
st.dataframe(ticker_df)
st.write('Daily closing price')
st.line_chart(ticker_df['Close'])

st.write('Volume')
st.line_chart(ticker_df['Volume'])
