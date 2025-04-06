# app.py
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="Aksh's AI Trading Assistant", layout="wide")

st.title("Aksh's AI Trading Assistant")

# Sidebar Controls
with st.sidebar:
    st.header("Settings")
    selected_index = st.selectbox("Select Index", ["NIFTY", "BANKNIFTY", "SENSEX"])
    stock_symbol = st.text_input("Stock Symbol (e.g. INFY.NS, TCS.NS)", value="RELIANCE.NS")
    lookback_days = st.slider("Lookback (Days)", 1, 30, 5)
    btst = st.checkbox("Show BTST Suggestions")

# Function to fetch data
@st.cache_data
def get_data(ticker, days):
    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=days)
    data = yf.download(ticker, start=start, end=end, interval="15m")
    return data

# Index Map
index_map = {
    "NIFTY": "^NSEI",
    "BANKNIFTY": "^NSEBANK",
    "SENSEX": "^BSESN"
}

index_data = get_data(index_map[selected_index], lookback_days)
stock_data = get_data(stock_symbol, lookback_days)

# Signal Generator (basic logic)
def generate_signals(df):
    df['MA20'] = df['Close'].rolling(20).mean()
    df['Signal'] = np.where(df['Close'] > df['MA20'], 'BUY', 'SELL')
    return df

index_data = generate_signals(index_data)
stock_data = generate_signals(stock_data)

# Live AI Commentary
st.subheader(f"Live Commentary - {selected_index}")
latest_signal = index_data['Signal'].iloc[-1]
latest_price = index_data['Close'].iloc[-1]
ai_comment = f"Currently, {selected_index} is showing a **{latest_signal}** signal around **₹{latest_price:.2f}**."

st.info(ai_comment)

# Chart
st.line_chart(index_data[['Close', 'MA20']])

# Stock Options Section
st.subheader("Stock Option Tracker with Greeks (Simulated)")
greek_sim = {
    'Delta': round(np.random.uniform(0.4, 0.8), 2),
    'Theta': round(np.random.uniform(-0.05, -0.01), 2),
    'Gamma': round(np.random.uniform(0.01, 0.15), 2)
}
st.write(f"**Symbol**: {stock_symbol}")
st.write(greek_sim)

# BTST Suggestion (if enabled)
if btst:
    btst_price = stock_data['Close'].iloc[-1]
    prev_close = stock_data['Close'].iloc[-2]
    if btst_price > prev_close:
        st.success(f"**BTST Opportunity:** Price has increased. Consider buying {stock_symbol} today.")
    else:
        st.warning(f"**No BTST Opportunity:** {stock_symbol} is not showing strength.")

# Footer
st.caption("Built for Aksh - Personal AI Trading Assistant")
