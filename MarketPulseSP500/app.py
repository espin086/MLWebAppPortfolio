import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.write("""
# MarketPulseSP500

Shown are the **closing price** and volume of the SPY!

""")

ticker = 'SPY'
data = yf.Ticker(ticker)
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=365*10)).strftime('%Y-%m-%d')
df = data.history(period='1d', start=start_date, end=end_date)

st.write("""
## Closing Price
""")
st.line_chart(df.Close)
st.write("""
## Volume
""")
st.line_chart(df.Volume)
